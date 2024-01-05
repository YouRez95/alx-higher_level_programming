#!/bin/bash
# display the http method allowed
curl -I -s $1 | grep -Fi "Allow" | cut -d' ' -f2-
