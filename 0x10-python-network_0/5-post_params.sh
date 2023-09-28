#!/bin/bash
#GET request to the URL A header variable X-School-User-Id
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
