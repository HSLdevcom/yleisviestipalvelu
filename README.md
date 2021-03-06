[![Build Status](https://travis-ci.org/HSLdevcom/yleisviestipalvelu.svg?branch=master)](https://travis-ci.org/HSLdevcom/yleisviestipalvelu)

## yleisviestipalvelu

### prerequisites

You must have an APR1 formatted password hash, which can be created with openssl(1):

    $ openssl passwd -apr1

### usage

Following assumes that you have build the Docker image and it is called `hsldevcom/yleisviestipalvelu`.

After building the image, you can run it with:

    $ docker run -d -e PORT=8900 -e HTPASSWD='user:$apr1$salt$hash' -p 8080:8080 hsldevcom/yleisviestipalvelu

When running the service in Swarm use a compose file such as:

    version: '3.3'

    services:
      yleisviesti:
        image: hsldevcom/yleisviestipalvelu
        ports:
        - "8080:8080"
        environment:
        - "PORT=8900"
        - "HTPASSWD=user:$apr1$salt$hash"
        volumes:
        - /local/path:/yleisviestipalvelu/messages
        deploy:
          replicas: 1
