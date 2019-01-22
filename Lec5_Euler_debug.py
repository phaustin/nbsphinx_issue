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
#       jupytext_version: 1.0.0-dev
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.7
#   nbsphinx:
#     execute: never
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: true
#     toc_position: {}
#     toc_section_display: true
#     toc_window_display: true
# ---

# %% [markdown] {"toc": "true"}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>
# %% [markdown]
# The choice of the timestep matters. Look at the previous equation:
#
# \begin{equation}
# \frac{\color{blue}{c_{\text{TMF}}}(t + \Delta t)-c_{\text{TMF}}(t)}{\Delta t} =  \frac{Q_{\text{pit}}  c_{\text{pit}} + Q_{\text{mill}}  c_{\text{mill}} + A_{\text{bottom}} k \left( c_{\text{pore}} - {\color{red}{c_{\text{TMF}}}}  \right)    -Q_{\text{dis}} \color{red}{c_{\text{TMF}}}}{V_0}
# \end{equation}
#
# To compute the solution $c_{\text{TMF}}(t+ \Delta t)$, we use the value of $c_{\text{TMF}}$. But, at what time? Intrinsically, at every time between $t$ and $ t + \Delta t$, the value of $c_{\text{TMF}}$ changes.
#
# So the timestep should be small!
# %% [markdown]
# \begin{equation}
# \begin{array}{lll}
# c_\infty & = & \frac{Q_{\text{pit}}  c_{\text{pit}} + Q_{\text{mill}}  c_{\text{mill}} + kA c_{\text{pore}} }{Q_{\text{dis}}+kA} \\
#  & = & \frac{\color{blue}{Q_{\text{pit}}  c_{\text{pit}}} + \color{blue}{Q_{\text{mill}}  c_{\text{mill}}} + kA c_{\text{pore}} }{\color{blue}{Q_{\text{dis}}}+kA} \\
#   & \approx & \frac{kA c_{\text{pore}} }{kA} \\
#  & \approx & c_{\text{pore}} = 2000 \text{ mg/L}
# \end{array}
# \end{equation}

# %%
