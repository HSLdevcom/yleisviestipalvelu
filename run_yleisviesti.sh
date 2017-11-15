#!/bin/sh

set -e

cd yleisviestipalvelu
mkdir -p messages/archive

echo "${HTPASSWD}" > /etc/nginx/auth.htpasswd
echo '{"staticMessages": []}' > messages/yleisviesti.json

python main.py --port=${PORT} --filename=messages/yleisviesti.json --filepath=messages/archive &

/usr/sbin/nginx
