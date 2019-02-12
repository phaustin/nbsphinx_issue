#!/bin/bash -v
rm -rf _build/*
sphinx-build -v -N -b html .  _build
jupyter nbconvert --to html img_fig_eq.ipynb --stdout >  _build/img_fig_eq_nbconvert.html
jupyter nbconvert --to html md_fig_eq_aligh.ipynb --stdout > _build/md_fig_eq_aligh_nbconvert.html
cp -a figures _build/.
