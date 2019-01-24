#!/bin/bash -v
sphinx-build -v -N -b html .  _build
jupyter nbconvert --to html Lec5_Euler_debug.ipynb
