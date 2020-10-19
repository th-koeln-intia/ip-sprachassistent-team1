#!/bin/sh

/usr/bin/crontab /crontab.txt && /usr/sbin/crond && echo "wwww" && flask run