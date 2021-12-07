# was855-todo-app-on-ocp
Todo Application - Websphere 8.5.5 Traditional on Openshift

# Pre-requisites

- JDK 8 (Java 1.8)
- maven
- Openshift >= 4.6.x
- Openshift CLI (`oc`) >= 4.6.x
- IBM Websphere Traditional Server 8.5.5
- IBM Transformation Advisor

# Deploy to Openshift

see [READ_THIS_FIRST](was855-todo-app-migration/READ_THIS_FIRST.md)

# Deploy Locally 

## Setup Postgresql

execute the following SQL scripts on your Postgresql Database server located in: 

```
├── was855-todo-app-migration
│   └── scripts
│       └── 01-database.sql
│       └── 02-schemas.sql
```

## Build, Deploy and Run

**Build the WAR file and package into an EAR file**

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

**Deploy the EAR file via any one of the following options:** 

- Websphere admin console 
  - Admin Console - https://localhost:9043/ibm/console/login.do?action=secure
    - [Example deployment walkthrough](https://www.youtube.com/watch?v=qg4lhtNiYtg)
- IDE 
  - [Intellij](https://www.jetbrains.com/help/idea/run-debug-configuration-websphere-server.html)
  - [IBM Rational Application Developer for WebSphere Software](https://www.ibm.com/products/rad-for-websphere-software)

**Setup JNDI in Websphere Application Server**

- Add a JDBC Provider

![Screenshot from 2021-12-07 10-19-42](https://user-images.githubusercontent.com/61749/145066535-19eee17a-4a32-44bd-98f5-5c9ea24cd8e8.png)

- Add a Data Source

![Screenshot from 2021-12-07 10-21-33](https://user-images.githubusercontent.com/61749/145066736-8f8350f0-3cab-4ffd-a5df-a77d3b84a530.png)


**Start the application server (if not started already)**

- start by command line:
  - `/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/startServer.sh server1`
- start via gui tools (installed via IBM Installation Manager)

**Validate your database connectivity by navigating to:** 

http://localhost:9080/was855-todo-app/dbtest-servlet

**Validate your application by navigating to:**

http://localhost:9080/was855-todo-app



