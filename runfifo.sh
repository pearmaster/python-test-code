#!/bin/bash


gcc fifo_gen.c -o fifo_gen

python3 fifo_echo.py /tmp/to_python /tmp/from_python &

./fifo_gen
