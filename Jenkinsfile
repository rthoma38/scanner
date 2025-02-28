pipeline {
    agent any
    environment {
        SONAR_RUNNER_HOME = '/home/jenkins/sonar-scanner'
        PATH = "${SONAR_RUNNER_HOME}/bin:${env.PATH}"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rthoma38/sonarqubedemo.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                // Add build steps if needed
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Add test steps if needed
            }
        }
        stage('Vulnerability Scan') {
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
    }
}
