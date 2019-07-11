#!/bin/sh

set -e

cd yleisviestipalvelu
mkdir -p messages/archive

echo "${HTPASSWD}" > /etc/nginx/auth.htpasswd
if [ ! -f "messages/yleisviesti.json" ]; then
    echo '{"staticMessages": []}' > messages/yleisviesti.json
fi

python main.py --port=${PORT} --filename=messages/yleisviesti.json --filepath=messages/archive/ &

/usr/sbin/nginx
