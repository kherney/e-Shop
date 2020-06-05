# e-Shop-
e-Commerce web employ bootstrap and Dj.ango

# website-docker
Full Stack web para lanzamiento de instancias de servidores odoo utilizando SDK-Docker y Django

## Instalacion de django


```sh
$ sudo apt update 
$ sudo apt upgrade
$ sudo apt install python3-dev python3-pip
$ sudo pip3 install virtualenv 
$ virtualenv -p python3 django-bin
```


```sh
$ pip3 install django djangorestframework markdown django-filter psycopg2
```

## Instalacion Docker

Update the apt package index and install packages to allow apt to use a repository over HTTPS:

```sh
$ sudo apt update 
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

```sh
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

```sh
 $ sudo apt-get update
 $ sudo apt-get install docker-ce docker-ce-cli containerd.io

```

```sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker 

```
```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

### Configurar Postgress 

```sh
docker-compose -f  web-engine.yml up -d
```

```sh
docker stop 
docker run 
docker ps 
```

## Lanzar servidor

```sh
python manager.py runserver
```