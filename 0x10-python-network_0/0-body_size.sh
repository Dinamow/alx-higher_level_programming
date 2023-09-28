#!/bin/bash
#displays the size of the body of the response
curl -so "$1" | wc -c
