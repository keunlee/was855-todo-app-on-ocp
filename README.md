# was855-todo-app-on-ocp
Todo Application - Websphere 8.5.5 Traditional on Openshift

# Pre-requisites

**Openshift Deployment**

- Openshift >= 4.6.x
- Openshift CLI (`oc`) >= 4.6.x
- IBM Transformation Advisor

**Local Deployment**

- JDK 8 (Java 1.8)
- maven
- Postgresql Database Server >= 14
- IBM Websphere Traditional Server 8.5.5

# Deploy to Openshift

Leveraging the IBM Transformation Advisor, the contents of `was855-todo-app-migration` are generated.

After artifact generation, you can tailor any facet of the artifacts generated to suit your deployment needs to Openshift.

see [OPENSHIFT_SETUP](was855-todo-app-migration)

# Deploy Locally

see [LOCAL_SETUP](docs/LOCAL_SETUP.md)

![Screenshot from 2021-12-07 10-41-13](https://user-images.githubusercontent.com/61749/145069982-5c546756-1eb4-4ac5-8879-f90023149f67.png)
