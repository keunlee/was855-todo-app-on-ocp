# wsadmin script generated by binaryAppScanner
# This configuration was migrated on 12/2/21 at 2:22:55 PM from the following location: /opt/IBM/WebSphere/AppServer/profiles/AppSrv01
# The binary scanner does not support the migration of all WebSphere traditional configuration elements. Check the binary scanner documentation for the list of supported configuration elements.

Cell=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/')
Node=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/')
Server=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/Server:server1')
NodeName=AdminControl.getNode()

# The following variables are used to replace sensitive data in the configuration for the application.
# The values for these variables were not collected because the includeSensitiveData option was not specified.
# ============================================================
ocp_project_namespace='demo-todo-was855-custom'
pg_datasource_password_1='postgres'
pg_datasource_user_1='postgres'
pg_datasource_host_1='postgres.' + ocp_project_namespace
# ============================================================

print 'Starting Creating JVM Properties'
# Properties are migrated from server localhostNode01/server1.
AdminTask.setJVMProperties(Server, ["-maximumHeapSize", "2048"])
AdminTask.setGenericJVMArguments('[-nodeName ' + NodeName + ' -serverName server1 -genericJvmArguments "-Dcom.ibm.xml.xlxp.jaxb.opti.level=3"]')

print 'Starting Creating Authentication Alias'

print 'Starting Creating Queues'

print 'Starting Creating Topics'

print 'Starting Creating Activation Specifications'

print 'Starting Creating Connection Factories'

print 'Starting Creating JDBC Providers'
AdminConfigVar_0=AdminConfig.create('JDBCProvider', Node, [['classpath', '/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/installedApps/DefaultCell01/was855todoappearear.ear/was855-todo-app-1.0-SNAPSHOT.war/WEB-INF/lib/postgresql-42.3.1.jar'], ['description', 'pgSQL_provider'], ['implementationClassName', 'org.postgresql.jdbc2.optional.ConnectionPool'], ['name', 'pgSQL_provider'], ['providerType', 'User-defined JDBC Provider'], ['xa', 'false']])
AdminConfigVar_1=AdminTask.createDatasource(AdminConfigVar_0, ["-name", "pg_datasource", "-jndiName", "pg", "-dataStoreHelperClassName", "com.ibm.websphere.rsadapter.ConnectJDBCDataStoreHelper"])
AdminConfigVar_2=AdminConfig.showAttribute(AdminConfigVar_1, 'propertySet')
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'databaseName'], ['type', 'java.lang.String'], ['value', 'todo']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'enableMultithreadedAccessDetection'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'errorDetectionModel'], ['type', 'java.lang.String'], ['value', 'ExceptionMapping']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'jmsOnePhaseOptimization'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'name'], ['type', 'java.lang.String'], ['value', 'pg_datasource']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'nonTransactionalDataSource'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'password'], ['type', 'java.lang.String'], ['value', pg_datasource_password_1]])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'portNumber'], ['type', 'int'], ['value', '5432']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'preTestSQLString'], ['type', 'java.lang.String'], ['value', 'SELECT 1 FROM DUMMYTABLE']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'reauthentication'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'serverName'], ['type', 'java.lang.String'], ['value', pg_datasource_host_1]])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'user'], ['type', 'java.lang.String'], ['value', pg_datasource_user_1]])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'validateNewConnection'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'validateNewConnectionRetryCount'], ['type', 'java.lang.Integer'], ['value', '100']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'validateNewConnectionRetryInterval'], ['type', 'java.lang.Long'], ['value', '3']])
AdminConfigVar_3=AdminConfig.showAttribute(AdminConfigVar_1, 'connectionPool')
AdminConfig.modify(AdminConfigVar_3, [['stuckThreshold', '0'], ['reapTime', '180'], ['testConnectionInterval', '0'], ['connectionTimeout', '180'], ['surgeCreationInterval', '0'], ['surgeThreshold', '-1'], ['stuckTimerTime', '0'], ['numberOfFreePoolPartitions', '0'], ['minConnections', '0'], ['unusedTimeout', '1800'], ['agedTimeout', '0'], ['numberOfSharedPoolPartitions', '0'], ['purgePolicy', 'EntirePool'], ['maxConnections', '10'], ['freePoolDistributionTableSize', '0'], ['stuckTime', '0'], ['testConnection', 'false'], ['numberOfUnsharedPoolPartitions', '0']])

print 'Starting Creating Variables'

print 'Starting Saving Configuration Changes Before Application Deployment'
AdminConfig.save()
print 'Starting Application Deployment'
AdminConfig.create('Library', Server, [['name', 'globalSharedLibrary'], ['classPath',  '/work/config/lib']])
appServer = AdminConfig.list('ApplicationServer',Server)
classLoader1 = AdminConfig.create('Classloader', appServer, [['mode',  'PARENT_FIRST']])
AdminConfig.create('LibraryRef', classLoader1, [['libraryName', 'globalSharedLibrary']])
#AdminApp.install('/path/to/was855-todo-app-ear_ear.ear', ["-node", NodeName, "-server", "server1", "-appname", "was855-todo-app-ear_ear.ear", "-CtxRootForWebMod", [["was855-todo-app-1.0-SNAPSHOT.war", "was855-todo-app-1.0-SNAPSHOT.war,WEB-INF/web.xml", "/was855-todo-app"]]])
AdminConfig.save()