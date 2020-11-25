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
- name: nhl-db

Para ingresar al panel de administración de la base de datos ejecutar el siguiente comando desde el usuario cc3201:
```
psql nhl-db
```

Para verificar que la base de datos se encuentre funcionando correctamente:
```
/etc/init.d/postgresql status
```
