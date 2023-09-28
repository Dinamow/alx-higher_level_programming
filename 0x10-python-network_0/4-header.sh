#!/bin/bash
#GET request to the URL A header variable X-School-User-Id
curl -s -H "X-School-User-Id:98" "$1"
