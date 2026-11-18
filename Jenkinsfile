pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t devops-python-app:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Deploying application'

                sh '''
                    docker rm -f devops-app || true

                    docker run -d \
                      --name devops-app \
                      --restart unless-stopped \
                      -p 5000:5000 \
                      devops-python-app:${BUILD_NUMBER}
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'curl --fail http://localhost:5000/health'
            }
        }
    }
}
