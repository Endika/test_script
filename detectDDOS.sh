#!/bin/bash
netstat -plan|grep :$1|awk {'print '}|cut -d: -f 1|sort|uniq -c|sort -nk 1
