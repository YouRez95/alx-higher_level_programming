#!/bin/bash
# comment
curl -s -w "%{size_download}\n" $1
