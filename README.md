# nhl-analysis
Data analysis project based on "Bases de Datos-CC3201" course

# Información general

## Conexión al servidor
- host: cc3201.dcc.uchile.cl
- usuario: cc3201
- clave: cah9chee3chu
- puerto ssh: 324

Usando cliente SSH linux, basta con ejecutar el siguiente comando e ingresar la clave.
```
ssh cc3201@cc3201.dcc.uchile.cl -p 324
```

## Base de datos

- owner: cc3201
- owner-password: sup3rs3cur3
- name: nhl-db

Para ingresar al panel de administración de la base de datos ejecutar el siguiente comando desde el usuario cc3201:
```
psql nhl-db
```

Para verificar que la base de datos se encuentre funcionando correctamente:
```
/etc/init.d/postgresql status
```
Para crear conexión a servidor desde pgAdmin, click derecho en [Servers]>[Create], luego especificar lo siguiente.
- En menu [General], especificar Name: cc3201bbdd
- En menu [Connection], especificar:
  - host: cc3201.dcc.uchile.cl
  - port: 5524
  - Maintenance database: nhl-db
  - Username: cc3201
  - Password: sup3rs3cur3
  
Finalmente guardar la conexión y debería realizarse automáticamente.
