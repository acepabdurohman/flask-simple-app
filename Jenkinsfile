pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.7.2' 
                }
            }
        }
        stage('test') {
          steps {
            sh 'python test_app.py'
          }    
        }
    }
}