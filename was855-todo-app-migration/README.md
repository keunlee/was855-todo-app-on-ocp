# Deploy to Openshift

## Generated Artifacts
| Artifact | Description |
| --- | --- |
| was855-todo-app-ear-1.0-snapshot.ear | Application binary ear, or war or jar file |
| Dockerfile | Dockerfile to build the application container image |
| src/config/install_app.py | Jython script to install the application |
| src/config/server_config.py | server configuration Jython script file |  
| lib/ | Directory for external library dependencies, such as database driver library | 
| pipeline/k8s/ | Directory for the application deployment manifest files |
| pipeline/openshift/ | Directory for OpenShift pipeline manifest files |

### Notes
- The pipeline artifacts for openshift are compatible with OpenShift >= 4.6.

- The generated `src/config/server_config.py` script file may contain password variables that you may need to reset. They are currently set for demo purposes.

  ```
  # variables
  # ============================================================
    ocp_project_namespace='demo-todo-was855'
    pg_datasource_password_1='postgres'
    pg_datasource_user_1='postgres'
    pg_datasource_host_1='postgres.' + ocp_project_namespace
  # ============================================================  
  ```

## Deploy to Red Hat OpenShift Container Platform using OpenShift Pipelines

### Prerequisites
1. 
2. Install the OpenShift Pipeline Operator if its not already installed. See OpenShift [documentation](https://docs.openshift.com/container-platform/4.6/pipelines/installing-pipelines.html) for more details.

### Steps - Build and Deploy

```bash
# login into openshift - oc login ...

# delete project if it exists and wait for it to terminate
oc delete project demo-todo-was855

# create project
oc new-project demo-todo-was855

# create pipeline, pipeline resources, and a pipeline run to trigger a pipeline
oc create -f was855-todo-app-migration/pipeline/openshift

# navigate to the route below after deployment
oc get routes
```

### References

https://github.com/WASdev/ci.docker.websphere-traditional#readme

https://github.com/WASdev/ci.docker.websphere-traditional/tree/master/samples/hello-world/openshift
