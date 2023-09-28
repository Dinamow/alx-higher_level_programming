#!/bin/bash
#displays the body of the response
curl -s -I -X OPTIONS "$1" | awk '/Allow:/ {print substr($0, 8)}'
