pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image('python:3.9').inside('-u root') {
                        sh '''
                            pip install -r requirements.txt
                            pytest
                        '''
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                   // Remove old containers with label 'my-flask-app'
                    sh 'docker rm -f $(docker ps -a -q --filter "label=my-django-app") || true'
                    
                    // Build and run new container
                    def dockerImage = docker.build("my-django-app:${env.BUILD_NUMBER}", '.')
                    dockerImage.run("-d -p 8000:8000 --label my-django-app") // Runs the Docker image in detached mode, mapping port 5000 on host to port 5000 in the container and adds the 'my-flask-app' label
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}