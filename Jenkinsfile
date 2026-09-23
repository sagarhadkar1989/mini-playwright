pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/mini-playwright.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install pytest playwright allure-pytest'
                sh '. venv/bin/activate && playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest --alluredir=reports/'
            }
        }

        stage('Publish Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'reports']]
                ])
            }
        }
    }
}
