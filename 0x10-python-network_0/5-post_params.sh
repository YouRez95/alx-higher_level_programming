#!/bin/bash
# send Post request with body
curl -s -X POST -d 'email=test@gmail.com&subject=I will always be here for PLD' $1
