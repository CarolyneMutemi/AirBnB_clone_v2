#!/usr/bin/env bash

if grep "hbnb_static" /etc/nginx/sites-available/default > /dev/null 2>&1; then
	echo "In"
else
	echo "Not"
fi
