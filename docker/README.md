# Docker

'''bash
docker build -t api_rest:10.06.22 .
'''

'''bash 
docker run -it -v "$PWD"/code:/home/code --net host --mane api_rest -h api_rest api_rest:10.06.22
'''