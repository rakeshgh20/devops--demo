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
                sh 'python3 -m unittest test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-demo:1.0 .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker rm -f devops-demo || true
                    docker run -d \
                      --name devops-demo \
                      -p 5000:5000 \
                      devops-demo:1.0
                '''
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
                sh 'curl --fail http://localhost:5000'
            }
        }
    }
}
