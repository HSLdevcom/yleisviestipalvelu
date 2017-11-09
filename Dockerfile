FROM nginx:mainline-alpine

ENV HTPASSWD='yleisviesti:$apr1$sM6OuSuR$aQ3xduEKmpDBmFx.QqrR1/'

RUN apk add --no-cache python
ADD https://bootstrap.pypa.io/get-pip.py get-pip.py

RUN python get-pip.py
RUN pip install tornado

COPY . /yleisviestipalvelu

ADD run_yleisviesti.sh run_yleisviesti.sh
RUN chmod +x run_yleisviesti.sh

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["./run_yleisviesti.sh"]