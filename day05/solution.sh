#!/bin/bash

bin_value=$(sed -e 's/F/0/g' -e 's/B/1/g' -e 's/R/1/g' -e 's/L/0/g' input.txt | sort | tail -n1)
# This line only exists to strip the following value from windows  character as bs got a problem with it:/
bin_value=$(echo "$bin_value" | tr -d $'\r')
echo "obase=10; ibase=2; $bin_value" | bc

sed -e 's/F/0/g' -e 's/B/1/g' -e 's/R/1/g' -e 's/L/0/g' input.txt | sort > "better_input.txt"
