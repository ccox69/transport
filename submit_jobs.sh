#!/bin/bash

for JNAME in $(ls)
do
   sbatch $JNAME
done
