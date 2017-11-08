FROM nginx:mainline-alpine

RUN apk add --no-cache python git curl
ADD https://bootstrap.pypa.io/get-pip.py get-pip.py

RUN python get-pip.py
RUN pip install tornado

RUN git clone https://github.com/pailakka/yleisviestipalvelu.git

ADD run_yleisviesti.sh run_yleisviesti.sh
RUN chmod +x run_yleisviesti.sh

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["./run_yleisviesti.sh"]