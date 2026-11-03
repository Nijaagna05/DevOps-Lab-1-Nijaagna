
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing application dependencies'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                bat 'python -m pytest tests -v --junitxml=reports\\junit.xml'
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
                echo 'Starting Flask application'

                powershell '''
                    $existing = Get-NetTCPConnection -LocalPort 5000 -State Listen -ErrorAction SilentlyContinue

                    if ($existing) {
                        $processIds = $existing | Select-Object -ExpandProperty OwningProcess -Unique
                        foreach ($processId in $processIds) {
                            Stop-Process -Id $processId -Force
                        }
                        Start-Sleep -Seconds 2
                    }

                    $python = (Get-Command python).Source
                    $process = Start-Process -FilePath $python `
                        -ArgumentList "application\\app.py" `
                        -WorkingDirectory $env:WORKSPACE `
                        -PassThru

                    Start-Sleep -Seconds 5

                    $response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/health"

                    if ($response.status -ne "healthy") {
                        throw "Deployment health check failed"
                    }

                    Write-Host "Deployment successful. PID: $($process.Id)"
                    Write-Host "Application health: $($response.status)"
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
            echo 'Pipeline execution finished.'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
