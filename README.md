
## yleisviestipalvelu

### prerequisites

You must have an APR1 formatted password hash, which can be created with openssl(1):

    $ openssl passwd -apr1

### usage

Following assumes that you have build the Docker image and it is called `yleisviesti`.

After building the image, you can run it with:

    $ docker run -d -e PORT=8900 -e HTPASSWD='user:$apr1$salt$hash' -p 8080:8080 yleisviesti

When running the service in Swarm use a compose file such as:

    version: '3.3'

    services:
      yleisviesti:
        image: yleisviesti
        ports:
        - "8080:8080"
        environment:
        - "PORT=8900"
        - "HTPASSWD=user:$apr1$salt$hash"
        volumes:
        - /local/path:/yleisviestipalvelu/messages
        deploy:
          replicas: 1
