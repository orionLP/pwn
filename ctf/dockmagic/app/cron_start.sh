#!/bin/bash
echo "Starting app" && /usr/sbin/sshd && service cron start
chown -R emp:emp /home/emp/app/*
su - emp -c "cd /home/emp/app && export GEM_HOME=/home/emp/.gems && rm -f tmp/pids/server.pid && RAILS_ENV=production bundle exec rails s -p 3000 -b '0.0.0.0'"
