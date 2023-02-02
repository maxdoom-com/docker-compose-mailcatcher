#!/bin/sh

cd /srv/mails
mini_httpd -h 0.0.0.0 -p 8080 -d .
python /sbin/mailcatcher.py

# sleep infinity
