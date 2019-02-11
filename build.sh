#!/bin/bash -v
rm -rf _build/*
sphinx-build -v -N -b html .  _build
jupyter nbconvert --to html img_fig_eq.ipynb --stdout >  img_fig_eq_nbconvert.html
jupyter nbconvert --to html md_fig_eq.ipynb --stdout > md_fig_eq_nbconvert.html
