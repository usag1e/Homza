#!/bin/bash

test=`sudo grep cors /etc/couchdb/local.ini`
if [ "$test" == '' ]; then
  echo 'Putting conf in local.ini'
  sudo cp /etc/couchdb/local.ini /etc/couchdb/local.ini.bak
  echo 'cat local.ini >> /etc/couchdb/local.ini' | sudo -s
fi

sudo service couchdb restart
echo 'Done'
