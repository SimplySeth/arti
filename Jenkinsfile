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