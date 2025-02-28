pipeline {
    agent any
    environment {
        SONAR_RUNNER_HOME = '/home/jenkins/sonar-scanner'
        PATH = "${SONAR_RUNNER_HOME}/bin:${env.PATH}"
    }

    stages {
        stage('Vulnerability Scan') {
            steps {
                sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image web-app'
            }
        }
        stage('Dynamic Vulnerability Scan with OWASP ZAP') {
            steps {
                sh '''
                docker run --name zap -u zap -p 8080:8080 -d zaproxy/zap zap.sh -daemon -port 8080
                docker exec zap zap-full-scan.py -t http://127.0.0.1 -r zap_report.html
                docker cp zap:/zap/zap_report.html ./zap_report.html
                docker stop zap
                docker rm zap
                '''
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube Scanner') {
                    sh 'sonar-scanner -Dsonar.projectKey=sonarqubeproject -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=$SONARQUBE_TOKEN'
                }
            }
        }
    }
}
