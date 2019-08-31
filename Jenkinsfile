pipeline {
    agent none 
    stages {pip install -r requirements.txt
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.7.2' 
                }
            }
            steps {
                sh """
                echo ${SHELL}
                [ -d venv ] && rm -rf venv
                #virtualenv --python=python2.7 venv
                virtualenv venv
                #. venv/bin/activate
                export PATH=${VIRTUAL_ENV}/bin:${PATH}
                pip install --upgrade pip
                pip install -r requirements.txt
                make clean
                """                
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml test_app.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}