#!/bin/bash
export PYTHONPATH=$PYTHONPATH:./src:.
python -m unittest discover -s src/tests 
