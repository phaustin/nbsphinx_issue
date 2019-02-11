# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: ''
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.0-rc3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# In 2-D, the general stencils for an interior gridblock C in terms of total flux, specific flux and concentrations are:
# \begin{align}
# &\left(J_{EC}+J_{WC} + J_{NC}+J_{SC}\right) = 0 \label{eq769}
# \end{align}
#
# \begin{align}
# &\left(j_{EC}+j_{WC}\right) (\Delta y) (\Delta z) +\left(j_{NC}+j_{SC}\right) (\Delta x) (\Delta z)  = 0 \label{eq7610}
# \end{align}
#
#
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   D\theta {c_W - c_C \over \Delta x}   \right) (\Delta y) (\Delta z)
# +\left(D\theta {c_N - c_C \over \Delta y} +   D\theta {c_S - c_C \over \Delta y}   \right) (\Delta x) (\Delta z)= 0 \label{eq7611}
# \end{align}
#
#
# <img src="figures/2d_flux.png" alt="pic05" width="20%" >
#
