#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static

if ! which nginx > /dev/null 2>&1; then
	sudo apt update
	sudo apt install nginx
fi
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "Hello there! I'm Mitten." | sudo tee /data/web_static/releases/test/index.html > /dev/null 2>&1
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup
replacement="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {"
if ! grep "hbnb_static" /etc/nginx/sites-available/default > /dev/null 2>&1; then
	sudo sed -i "0,/location \/ {/s||$replacement|" /etc/nginx/sites-available/default
fi
sudo service nginx restart
