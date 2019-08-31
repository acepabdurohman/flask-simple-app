pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.7.2' 
                }
            }
            steps {
                sh """                
                source venv/bin/activate
                pip install -r requirements.txt
                """
            }
        }
        stage('test') {
          steps {
            sh 'python test_app.py'
          }    
        }
    }
}