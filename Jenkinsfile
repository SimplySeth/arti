properties([
  parameters([
    [$class: 'ChoiceParameter',
    choiceType: 'PT_SINGLE_SELECT',
     description: 'Select your portfolio',
     filterLength: 1,
     filterable: true,
     name: 'Portfolio',
     script: [
       $class 'GroovyScript',
       fallbackScript: [
         classpath: [],
         sandbox: false,
         script:
          'return[\'Could not get Portfolio\']'
       ],
       script: [
         classpath: [],
         sandbox: true,
         script: showPortfolios()
       ]
     ]
  ])
])

pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        ws(dir: 'Build') {
          cleanWs(cleanWhenAborted: true, cleanWhenSuccess: true, cleanWhenUnstable: true, cleanupMatrixParent: true, deleteDirs: true, cleanWhenNotBuilt: true, cleanWhenFailure: true, disableDeferredWipeout: true, skipWhenFailed: true)
        }

      }
    }

  }
}
  
def showPortfolios() {
    return ['K8S','K8SL']
  }
