# Docker

# Crear la imagen
'''bash
docker build -t api_rest:10.06.22 .
'''

# Crear un contenedor 
'''bash 
docker run -it -v "$PWD"/code:/home/code --net host --mane api_rest -h api_rest api_rest:10.06.22
'''