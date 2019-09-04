pipeline {
    agent {
        docker {
            image 'python:3.6' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh 'echo $HOME'
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'echo $HOME'
                    sh 'pip install -r requirements.txt'
                }                
            }
        }
        stage('Test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python test_app.py'
                }                
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
        stage('SonarQube analysis') {
            steps {
                def scannerHome = tool 'SonarScanner 4.0';
                withSonarQubeEnv('sonarqube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }
}
