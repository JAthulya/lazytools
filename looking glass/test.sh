#!/bin/bash
echo "hello"
ip=10.10.123.99
#port=11000
for i in $ran
do
	echo "script port is $i"
	ssh -o HostKeyAlgorithms=+ssh-rsa -o StrictHostKeyChecking=no $ip -p $i
done
