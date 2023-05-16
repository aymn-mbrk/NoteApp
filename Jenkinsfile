pipeline {
  agent any
  
  stages {
    stage('Checkout') {
      steps {
        // Récupère les playbooks Ansible depuis le dépôt Git
        checkout([$class: 'GitSCM', 
          branches: [[name: 'Production']], 
          doGenerateSubmoduleConfigurations: false, 
          extensions: [], 
          submoduleCfg: [], 
          userRemoteConfigs: [[url: 'git@github.com:HimeYN/NoteApp.git']]
        ])
      }
    }   

    stage('Deploiement') {
      agent { node { label 'ansible'} }
      environment {
        // Définit les variables d'environnement pour l'utilisateur distant et les informations d'authentification SSH
        remoteUser = 'ubuntu'
        sshKey = credentials('77844eb2-4a70-4321-b9ab-940fbef837a2')
      }      
      steps {
        // Exécute les commandes Ansible pour déployer les playbooks sur l'agent distant
        withEnv(["ANSIBLE_CONFIG=ansible/ansible.cfg"]) {
          sh "ansible-playbook -i ansible/inventory ansible/docker.yml"
        }
      }
    }
  }
}
