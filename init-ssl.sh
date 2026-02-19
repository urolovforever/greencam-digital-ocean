#!/bin/bash
# Run this script ONCE on your Digital Ocean server to get the initial SSL certificate.
# Usage: bash init-ssl.sh

set -e

DOMAIN="greencam.uz"
EMAIL="${1:?Usage: bash init-ssl.sh your-email@example.com}"

echo "==> Step 1: Starting nginx with HTTP-only config..."

# Temporarily replace nginx.conf to only serve HTTP (no SSL yet)
cat > /tmp/nginx-temp.conf <<'NGINX'
upstream django {
    server web:8000;
}
server {
    listen 80;
    server_name greencam.uz www.greencam.uz;
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }
    location / {
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
NGINX

# Back up real config and use temp one
cp nginx/nginx.conf nginx/nginx.conf.bak
cp /tmp/nginx-temp.conf nginx/nginx.conf

docker-compose up -d nginx

echo "==> Step 2: Requesting certificate from Let's Encrypt..."

docker-compose run --rm --entrypoint "certbot certonly --webroot --webroot-path=/var/www/certbot --email $EMAIL --agree-tos --no-eff-email -d $DOMAIN -d www.$DOMAIN" certbot

echo "==> Step 3: Restoring full SSL nginx config..."

# Restore the real nginx config with SSL
cp nginx/nginx.conf.bak nginx/nginx.conf
rm nginx/nginx.conf.bak

echo "==> Step 4: Restarting all services..."

docker-compose down
docker-compose up -d

echo ""
echo "Done! Your site should now be available at https://$DOMAIN"
echo "Certbot will auto-renew certificates in the background."
