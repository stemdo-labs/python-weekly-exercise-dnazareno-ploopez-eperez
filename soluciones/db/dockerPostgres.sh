#Para levantar la imagen de postgres, primero hay que pararse en la carpeta "db" dentro de "Soluciones"
#Luego ejecutar
docker build -t ejerfinal-db .

#Para levantar los contenedores de la imagen de Postgres creada y de Adminer, hay que situarse en la misma carpeta
#Luego ejecutar
docker-compose up -d