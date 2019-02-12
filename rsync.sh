#!/bin/bash -v
rsync -avz _build/* kiteh:/home/phil/public_html/github/nbsphinx/.
rsync -avz _build/*nbconvert*html kiteh:/home/phil/public_html/github/nbsphinx/nbconvert/.
rsync -avz _build/figures kiteh:/home/phil/public_html/github/nbsphinx/nbconvert/
