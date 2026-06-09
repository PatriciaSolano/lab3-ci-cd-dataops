pipeline {
    agent any

    stages {

        stage('Validar Python') {
            steps {
                bat 'py --version'
            }
        }

        stage('Ejecutar procesamiento') {
            steps {
                bat 'py scripts/procesamiento.py'
            }
        }

        stage('Finalizar') {
            steps {
                echo 'Pipeline ejecutado correctamente'
            }
        }
    }
}