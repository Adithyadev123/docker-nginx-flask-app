pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Adithyadev123/docker-nginx-flask-app.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh 'docker-compose down || true'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful 🚀'
        }
        failure {
            echo 'Deployment failed ❌'
        }
    }
}

