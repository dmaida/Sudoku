#!/bin/bash

while read line
	do
		max=1
		for i in `seq 1 $max`
		do
			python3 main.py backtracking_prime "$line"
		done


	done < 5.txt
