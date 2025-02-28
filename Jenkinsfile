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
                # Start the local ZAP instance
                C:\\Users\\rthom\\OneDrive\\Desktop\\ZAP_WEEKLY\\ZAP_D-2025-02-26\\zap.sh -daemon -port 8081

                # Wait for ZAP to start up (adjust the sleep time if necessary)
                sleep 10

                # Run the full scan
                python C:\\Users\\rthom\\OneDrive\\Desktop\\ZAP_WEEKLY\\ZAP_D-2025-02-26\\zap-full-scan.py -t http://127.0.0.1:5000 -r zap_report.html

                # Stop the ZAP instance
                C:\\Users\\rthom\\OneDrive\\Desktop\\ZAP_WEEKLY\\ZAP_D-2025-02-26\\zap.sh -shutdown
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
