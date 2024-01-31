#!/usr/bin/env bash
# script that sets up my web servers for the deployment

apt-get update
#-y for auto agree
apt-get install -y nginx
#-p parent directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<h1> hey </h1>" > /data/web_static/releases/test/index.html
#-f for 'recreated every time the script is ran'
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
	alias /data/web_static/current;
	index index.html index.htm;
    }

        location /redirect_me {
	return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
