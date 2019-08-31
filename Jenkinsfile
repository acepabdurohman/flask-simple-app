pipeline {
    agent {
        docker {
            image 'python:3.6' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                }                
            }
        }
        stage('test') {
            steps {
                sh 'python -m unittest test_app.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
    }
}