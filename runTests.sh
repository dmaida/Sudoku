#!/bin/bash

while read line
	do
		max=3
		for i in `seq 1 $max`
		do
			python3 nn_sudoku.py "$line"
		done
		cp timeResults.txt Times/$line
		rm timeResults.txt

	done < puzzles.txt

