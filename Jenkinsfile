properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/shlomiunger/DevOps0909.git"
    }
    stage("show files"){
        bat "dir"
        
    }
}
