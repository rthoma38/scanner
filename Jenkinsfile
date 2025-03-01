pipeline {
    agent any
    environment {
        SONAR_RUNNER_HOME = '/home/jenkins/sonar-scanner'
        PATH = "${SONAR_RUNNER_HOME}/bin:${env.PATH}"
        ZAP_API_KEY = credentials('ZAP_API_KEY') // Use the credentials ID you set in Jenkins
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/rthoma38/scanner.git'

            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install python-owasp-zap-v2.4
                    pip install pytest pytest-cov
                '''
            }
       }
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --cov=prime --cov-report=xml
                '''
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube Scanner') {
                    sh 'sonar-scanner -Dsonar.projectKey=sonarqubeproject -Dsonar.sources=prime.py -Dsonar.exclusions=venv/** -Dsonar.host.url=http://localhost:9000 -Dsonar.login=$SONARQUBE_TOKEN -Dsonar.python.coverage.reportPaths=coverage.xml'
                }
            }
        }
        stage('Dynamic Vulnerability Scan - OWASP ZAP') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 zap_scan.py
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'zap_report.html', allowEmptyArchive: true
                }
            }
        }
    }
}
