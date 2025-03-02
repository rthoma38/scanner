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
                dir('tensorflow') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube Scanner') {
                    sh 'sonar-scanner -Dsonar.projectKey=SonarQube_Analysis -Dsonar.sources=. -Dsonar.exclusions=venv/** -Dsonar.host.url=http://localhost:9000 -Dsonar.login=${SONARQUBE_TOKEN}'
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                dir('tensorflow') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r ../anomaly_detection/requirements.txt
                        python train_anomaly_detection_model.py
                        python deploy_anomaly_detection_api.py
                    '''
                }
            }
        }

        stage('Dynamic Vulnerability Scan - OWASP ZAP') {
            steps {
                dir('midterm') {
                    sh '''
                        . venv/bin/activate
                        python3 zap_scan.py
                    '''
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'anomaly_detection/zap_report.html', allowEmptyArchive: true
                }
            }
        }

        stage('Vulnerability Scan - Trivy') {
            steps {
                sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image web-app'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/*.html', allowEmptyArchive: true
            junit 'test-reports/**/*.xml'
        }
    }
}
