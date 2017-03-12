#!/bin/bash

while read line
	do
		max=1
		for i in `seq 1 $max`
		do
			 ./main.py backtracking "$line"
		done


	done < Puzzles/5.txt
