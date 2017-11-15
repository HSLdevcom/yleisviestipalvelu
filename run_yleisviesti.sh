#!/bin/sh
cd yleisviestipalvelu
mkdir -p messages/archive
echo "{\"staticMessages\": []}" > messages/yleisviesti.json
python main.py --port=8900 --filename=messages/yleisviesti.json --filepath=messages/archive & > /dev/null

echo ${HTPASSWD} > /etc/nginx/auth.htpasswd

nginx
