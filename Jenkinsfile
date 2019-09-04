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
        stage('SonarQube') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh "/home/jenkins/tools/hudson.plugins.sonar.SonarRunnerInstallation/sonarqubescanner/bin/sonar-scanner -Dsonar.host.url=http://localhost:9000 -Dsonar.projectName=meanstackapp -Dsonar.projectVersion=1.0 -Dsonar.projectKey=meanstack:app -Dsonar.sources=. -Dsonar.projectBaseDir=/home/jenkins/workspace/Demo"
                }
                timeout(time: 10, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
