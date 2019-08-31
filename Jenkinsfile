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
                pip install virtualenv
                virtualenv --no-site-packages .
                source bin/activate
                pip install -r app/requirements.pip
                deactivate
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