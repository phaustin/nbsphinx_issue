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
# # Equation only

# %% [markdown]
# Therefore, for line $i$, representing the $i^{th}$ gridblock, the value for the $i-1$ columnn of matrix $A$ should be
# \begin{equation}
# A\left[i \right]\left[i-1 \right] = + \frac{D\theta}{\Delta x}\Delta y \Delta z
# \end{equation}
#
# The value representing the contribution from the cell on the right ($i+1$ column) is
# \begin{equation}
# A\left[i \right]\left[i+1 \right] = + \frac{D\theta}{\Delta x}\Delta y \Delta z
# \end{equation}
#
# And the term on the diagonal is
# \begin{equation}
# A\left[i \right]\left[i\right] = -2 \frac{D\theta}{\Delta x}\Delta y \Delta z
# \end{equation}
