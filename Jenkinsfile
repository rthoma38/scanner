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
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Setup') {
            steps {
                script {
                    // Set up virtual environment
                    sh '''
                        cd anomaly_detection
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
                    sh '''
                        cd anomaly_detection
                        sonar-scanner -Dsonar.projectKey
