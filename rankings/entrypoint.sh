#!/bin/sh

DB_URL_VALUE=$(printenv DB_URL)
echo "57 11 * * 4 export DB_URL=$DB_URL_VALUE; cd /issf_world_rankings/rankings && /usr/local/bin/python __main__.py >> /issf_world_rankings/rankings/cronlogfile.log 2>&1" | crontab -
cron -f -l 2
