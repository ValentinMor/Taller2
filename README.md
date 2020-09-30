# Taller2
Taller 2 - Redes y Servicios

1.- Montar imagen docker del servidor

  docker pull nodemailer/wildduck
  
2.- Iniciar servidor en docker

  sudo docker run --network=host nodemailer/wildduck
  
3.- Instalar dependencias

  npm install
  
4.- Crear usuario en wild duck

curl -i -XPOST http://localhost:8080/users \
-H 'Content-type: application/json' \
-d '{
  "username": "myuser",
  "password": "verysecret",
  "name": "John Doe",
  "address": "john.doe@example.com",
  "tags": [
    "status:regular_user",
    "subscription:business_big"
  ]
}'

5.- Ejecutar cliente

  node manage-mailbox.js
