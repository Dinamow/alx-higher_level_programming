#!/bin/bash
#displays only the status code
curl -o /dev/null -s -w "%{http_code}" $1
