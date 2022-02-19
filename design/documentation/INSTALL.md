# Instalação

## Ambiente

Esse projeto foi desenvolvido e testado em um Windows 11, mas deve funcionar também em Linux porque ele roda em cima de um Ubuntu 20.04 WSL2.

## Configure o WSL2 no Windows

Abra o PowerShell com elevação de Administrador e rode o seguinte comando para ativar o WSL.

        Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform, Microsoft-Windows-Subsystem-Linux

Após, defina o WSL 2 como padrão.

        wsl --set-default-version 2

Por último, instale o WSL.

        wsl --install


## Docker Client

Instale o Docker Client.

Ative o suporte ao WSL2.

Ative o Kubernetes.

## Kubernetes NGINX Ingress

Para instalar o NGINX Ingress utilize os seguintes comandos no Ubuntu.

        kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.30.0/deploy/static/mandatory.yaml
        kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.30.0/deploy/static/provider/cloud-generic.yaml


## Clone esse repositório

Caso você não tenha o git instalado no Ubuntu, execute o seguinte comando.

        sudo apt install git:1:2.25.1-1ubuntu3

Clone o repositório

        git clone https://github.com/joaofelipecb/hackthon.ifood

Entre dentro de repositório

        cd hackthon.ifood

## Python 3.8

Abra o Ubuntu 20.04 WSL2.

Atualize seu apt.

        sudo apt update

Instale o Python 3.8.

        sudo apt install python3.8:3.8.2-1ubuntu1

Instale o Python Virtualenv

        sudo apt install virtualenv:20.0.17-1

Crie um ambiente python

        virtualenv data/python/dev

Entre no ambiente virtual

        source data/python/dev/bin/activate

Instale os requirements.txt

        python -m pip install -r data/python/dev/requirements.txt

## Execute o Script de Inicialização

Para executar o Script de Inicialização, execute o seguinte comando.

        python data/script/dev/init.py
