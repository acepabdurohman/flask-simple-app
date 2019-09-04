node {
  stage('SCM') {
    git 'https://github.com/acepabdurohman/flask-simple-app.git'
  }
  stage('SonarQube Anal') {
    def scannerHome = tool 'SonarQubeScanner';
    withSonarQubeEnv('sonarqube') {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
