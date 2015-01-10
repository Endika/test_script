#!/bin/bash
# Force auto repair or delete fix fragment

help='fsck_force.sh <device>'

if [[ $1 = -h || $1 = --help ]]
then
    echo "$help"
    exit
fi

echo "Start to repair the $1"
sudo yes 1 | sudo fsck $1 -w -r
echo "End to repair the $1"
echo "Bye"
