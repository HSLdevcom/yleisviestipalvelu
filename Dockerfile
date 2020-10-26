FROM nginx:mainline-alpine

RUN apk add --no-cache python2 py-pip

RUN pip install tornado

COPY run_yleisviesti.sh run_yleisviesti.sh
COPY nginx.conf /etc/nginx/nginx.conf
COPY . /yleisviestipalvelu

RUN chmod +x run_yleisviesti.sh

EXPOSE 8080

CMD ["./run_yleisviesti.sh"]
