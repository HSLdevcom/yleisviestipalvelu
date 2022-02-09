[![Build](https://github.com/hsldevcom/yleisviestipalvelu/workflows/Process%20master%20push%20or%20pr/badge.svg?branch=master)](https://github.com/HSLdevcom/yleisviestipalvelu/actions)

## yleisviestipalvelu

### prerequisites

You must have an APR1 formatted password hash, which can be created with openssl(1):

    $ openssl passwd -apr1

### running the service

Following assumes that you have build the Docker image and it is called `hsldevcom/yleisviestipalvelu`.

After building the image, you can run it with:

    $ docker run -d -e HTPASSWD='user:$apr1$salt$hash' -p 8080:8080 hsldevcom/yleisviestipalvelu

When running the service in Swarm use a compose file such as:

    version: '3.3'

    services:
      yleisviesti:
        image: hsldevcom/yleisviestipalvelu
        ports:
        - "8080:8080"
        environment:
        - "HTPASSWD=user:$apr1$salt$hash"
        volumes:
        - /local/path:/yleisviestipalvelu/messages
        deploy:
          replicas: 1

### usage

User interface for managing message content is available in path /ui/edit
(e.g. https://matka-yleisviesti.digitransit.fi/ui/edit).

Editing endpoint requires basic authentication - use the password from hash generation step above. If the password
gets forgotten, generate a new one. It is not possible to extract the password from the hash.

Messages can be read from the service root path (e.g. https://matka.yleisviesti.digitransit.fi).
