#!/usr/bin/env bash
kill -0 $1 


while [ $? -eq 0 ]; do
	sleep 1
	kill -0 $1 


done
