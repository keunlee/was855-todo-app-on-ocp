# was855-todo-app-on-ocp
Todo Application - Websphere 8.5.5 Traditional on Openshift

## Pre-requisites

- JDK 8 (Java 1.8)
- maven
- Openshift >= 4.6.x
- Openshift CLI (`oc`) >= 4.6.x
- IBM Websphere Traditional Server 8.5.5
- IBM Transformation Advisor

## Deploy to Openshift

see [READ_THIS_FIRST](was855-todo-app-migration/READ_THIS_FIRST.md)

## Build, Deploy and Run (Locally)

Build the WAR file and package into an EAR file

```bash
mvn clean install package
```
The resulting build will show in the following target folders: 

```bash
├── was855-todo-app
│   └── target
│       └── was855-todo-app-1.0-SNAPSHOT.war
├── was855-todo-app-ear
│   └── target
│       └── was855-todo-app-ear-1.0-SNAPSHOT.ear
```

Deploy the EAR file via any one of the following options: 

- Websphere admin console 
  - Admin Console - https://localhost:9043/ibm/console/login.do?action=secure
    - [Example deployment walkthrough](https://www.youtube.com/watch?v=qg4lhtNiYtg)
- IDE 
  - [Intellij](https://www.jetbrains.com/help/idea/run-debug-configuration-websphere-server.html)
  - [IBM Rational Application Developer for WebSphere Software](https://www.ibm.com/products/rad-for-websphere-software)

