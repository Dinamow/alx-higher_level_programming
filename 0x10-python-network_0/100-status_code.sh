#!/bin/bash
#displays only the status code
curl -s -I -X OPTIONS "$1" | awk '/HTTP\/1.1/ {printf $2}'
