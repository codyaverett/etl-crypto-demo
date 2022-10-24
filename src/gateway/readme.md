# Gateway

- Uses Nginx to reverse proxy to several project backend
- Uses LetsEncrypt to manage and install TLS/SSL Certificates

## Setup

- Install `nginx` and `nginx-mod-stream` packages
- Use the configurations found in this directory to configure the server.  Change as required

### Certificates

- Install `certbot` and `certbot-nginx`
- Run `certbot` and follow the prompts

> Certbot should be able to find any servers you configure through nginx automatically.

## Todo

- Create an nginx container to minimize manual setup steps