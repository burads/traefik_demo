# traefik_demo

Simple demo of how to get traefik set up with a few different sub aplications.

this example has the dns names traefik.example.com and introvert.example.com setup to point to the two services. these can be setup as administrator in your hosts file
Windows: ´c:\Windows\System32\Drivers\etc\hosts´
Linux: ´/etc/hosts´

there are two folders with docker-compose files
traefik and traefiktest.
traefik only sets up the base image as well as connects to the "private" network web.
traefiktest contains a test python image that sets a flask web server that both connects internally and repies with info about the service and neithbours in a json object.

´´´{
  "neighbours": {
    "api:8080": {
      "actuator": "/actuator/health",
      "status": "200"
    },
    "frontend:8080": {
      "actuator": "/actuator/health",
      "status": "200"
    },
    "head:8080": {
      "actuator": "/actuator/health",
      "status": "200"
    }
  },
  "server_info": {
    "hostname": "6d9db0247785",
    "ip_address": "172.19.0.2",
    "servername": "api",
    "uname": {
      "architecture": [
        "64bit",
        "ELF"
      ],
      "machine": "x86_64",
      "node": "6d9db0247785",
      "processor": "",
      "system": "Linux"
    }
  }
}´´´

## Usage
So use the application you only need to first start trafic in 
traefik$ ´docker-compose up´
then go to traefiktest 
if you have not yet build the base image do
traefiktest$ ´docker build . -t pyflaskserver:latest´
then you can start the images using 
traefiktest$ ´docker-compose up´