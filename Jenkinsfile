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
                    sh 'python test_app.py'
                }                
            }
        }
    }
}