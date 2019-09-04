node {
  stage('SCM') {
    git 'https://github.com/acepabdurohman/flask-simple-app.git'
  }
  stage('SonarQubeScanner') {
    def scannerHome = tool 'SonarScanner 4.0';
    withSonarQubeEnv('sonarqube') {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
