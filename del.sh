#!/bin/bash
replacement="location /hbnb_static/ {\n\t\talias /data/web_static/current/\n\t}\n\n\tlocation / {"
sed "0,/location \/ {/s||$replacement|" /etc/nginx/sites-available/default
