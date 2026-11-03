pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking source code'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                bat 'python -m pytest tests -v'
            }
        }

        stage('Package') {
            steps {
                echo 'Compiling application'
                bat 'python -m compileall -q application'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage will be configured next'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
