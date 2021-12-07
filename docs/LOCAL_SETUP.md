# Deploy Locally

## Setup Postgresql

execute the following SQL scripts on your Postgresql Database server located in:

```bash
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

**Start the application server (if not started already)**

- start by command line:
    - `/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/startServer.sh server1`
- start via gui tools (installed via IBM Installation Manager)

**Setup JNDI in Websphere Application Server**

You will need to have a copy of the Postgres Driver Library at hand to point to in the JNDI setup classpath below. see:

```bash
├── was855-todo-app-migration
│   └── lib
│       └── postgresql-42.3.1.jar
```

- Add a JDBC Provider

![Screenshot from 2021-12-07 10-19-42](https://user-images.githubusercontent.com/61749/145066535-19eee17a-4a32-44bd-98f5-5c9ea24cd8e8.png)

- Add a Data Source

![Screenshot from 2021-12-07 10-21-33](https://user-images.githubusercontent.com/61749/145066736-8f8350f0-3cab-4ffd-a5df-a77d3b84a530.png)

**Deploy the EAR file**

- Websphere Admin Console - https://localhost:9043/ibm/console/login.do?action=secure
- [Example: Websphere app deployment walkthrough](https://www.youtube.com/watch?v=qg4lhtNiYtg)

**Validate your database connectivity by navigating to:**

http://localhost:9080/was855-todo-app/dbtest-servlet

**Validate your application by navigating to:**

http://localhost:9080/was855-todo-app