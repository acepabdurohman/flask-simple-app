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
                sh """
                pip install -r requirements.txt
                """                
            }
        }
    }
}