properties([
  parameters([
    [$class: 'ChoiceParameter', 
     choiceType: 'PT_SINGLE_SELECT', 
     filterLength: 1, 
     filterable: true, 
     name: 'Portfolio', 
     randomName: 'choice-parameter-62045131134436', 
     script: [
       $class: 'GroovyScript', fallbackScript: [
         classpath: [], oldScript: '', sandbox: false, script: ''], 
       script: [
         classpath: [], oldScript: '', sandbox: true, script: '''return  ["K8S","K8SL"]'''
       ]
     ]
    ]
  ])
])

pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo "${params.Portfolio}"
      }
    }
  }
}
  
def showPortfolios() {
    return ['K8S','K8SL']
  }
