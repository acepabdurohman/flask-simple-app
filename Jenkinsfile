pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.6' 
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                }                
            }
        }
        stage('Test') {
            steps {
                sh 'python test_app.py'
            }
        }
    }
}