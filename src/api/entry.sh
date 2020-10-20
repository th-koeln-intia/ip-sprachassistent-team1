#!/bin/sh

/usr/bin/crontab /crontab.txt && /usr/sbin/crond && flask run