#!/bin/bash
#sends a JSON POST request, and displays the body of the response.
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
