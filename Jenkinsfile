pipeline {
    agent any
    environment {
        SONAR_RUNNER_HOME = '/home/jenkins/sonar-scanner'
        PATH = "${SONAR_RUNNER_HOME}/bin:${env.PATH}"
        ZAP_HOME = '/home/jenkins/ZAP_WEEKLY/ZAP_D-2025-02-26' // Path to ZAP installation
        ZAP_API_KEY = '5n6finf2qiu7536fdleme108c6' // Replace with your actual API key
    }

    stages {
        stage('Vulnerability Scan - Trivy') {
            steps {
                sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image web-app'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube Scanner') {
                    sh 'sonar-scanner -Dsonar.projectKey=sonarqubeproject -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=$SONARQUBE_TOKEN'
                }
            }
        }
        stage('Dynamic Vulnerability Scan - OWASP ZAP') {
            steps {
                sh '''
                    export ZAP_HOME=${ZAP_HOME}
                    export PATH=${ZAP_HOME}:${PATH}
                    ${ZAP_HOME}/zap.sh -daemon -host 127.0.0.1 -port 8081 -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true
                    sleep 10 # Wait for ZAP to start
                    ${ZAP_HOME}/zap-cli quick-scan --self-contained --start-options "-config api.key=${ZAP_API_KEY}" http://localhost:5000
                    ${ZAP_HOME}/zap-cli report -o zap_report.html -f html
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
