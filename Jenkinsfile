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
                dir('anomaly_detection') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                dir('anomaly_detection') {
                    withSonarQubeEnv('SonarQube Scanner') {
                        sh 'sonar-scanner -Dsonar.projectKey=SonarQube_Analysis -Dsonar.sources=. -Dsonar.exclusions=venv/** -Dsonar.host.url=http://localhost:9000 -Dsonar.login=${SONARQUBE_TOKEN}'
                    }
                }
            }
        }

        stage('Dynamic Vulnerability Scan - OWASP ZAP') {
            steps {
                dir('anomaly_detection') {
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
                dir('anomaly_detection') {
                    sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image web-app'
                }
            }
        }

        stage('Data Collection') {
            steps {
                dir('anomaly_detection') {
                    sh '''
                        . venv/bin/activate
                        python3 collect_network_data.py
                    '''
                }
            }
        }

        stage('Train Model') {
            steps {
                dir('anomaly_detection') {
                    sh '''
                        . venv/bin/activate
                        python3 train_model.py
                    '''
                }
            }
        }

        stage('Save Model') {
            steps {
                dir('anomaly_detection') {
                    sh '''
                        . venv/bin/activate
                        python3 save_model.py
                    '''
                }
            }
        }

        stage('Deploy Model') {
            steps {
                dir('anomaly_detection') {
                    sh '''
                        . venv/bin/activate
                        python3 app.py
                    '''
                }
            }
        }

        stage('Test Model') {
            steps {
                dir('anomaly_detection') {
                    sh '''
                        . venv/bin/activate
                        python3 test_model.py
                    '''
                }
            }
        }
    }
}
