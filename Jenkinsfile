pipeline {
    agent any

    stages {

        stage('Validar Python') {
            steps {
                bat '"C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" --version'
            }
        }

        stage('Ejecutar procesamiento') {
            steps {
                bat '"C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" scripts\\procesamiento.py'
            }
        }

        stage('Finalizar') {
            steps {
                echo 'Pipeline ejecutado correctamente'
            }
        }
    }
}