#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:02:48 2024

@author: ard000
"""

import matplotlib.pyplot as plt
import numpy as np

save_figs = False
figdir = 'path/to/figure'

n1_all = np.array([4, 10, 25, 50])
n2_all = np.array([8, 20, 50, 100])

def pi(alpha_inf, n1, n2):
    return (n1 * alpha_inf + 1)**(-1) * ((n1 - n2) / n2)

alpha_inf_1_lab = np.around(np.arange(0.2, 1.0 + 0.1, 0.1), 1)
alpha_inf_2_lab = np.around(np.arange(1.5, 5.0 + 0.5, 0.5), 1)
alpha_inf_all_lab = np.concatenate((alpha_inf_1_lab, alpha_inf_2_lab))

alpha_inf_all_lab_major = np.array([0.2, 0.4, 0.6, 1.0, 1.5, 3.0, 5.0])

alpha_inf_1 = np.arange(0.2, 1.0 + 0.01, 0.01)
alpha_inf_2 = np.arange(1.01, 5.0 + 0.01, 0.01)
alpha_inf_all = np.concatenate((alpha_inf_1, alpha_inf_2))

# Define variables for known values

x_min = alpha_inf_all.min()
x_max = alpha_inf_all.max()

fig = plt.figure(num=1, figsize=(6, 4))
plt.clf()
ax = fig.add_subplot(111)
lines = []
for count, (n1, n2) in enumerate(zip(n1_all, n2_all)):
    pi_curr = pi(alpha_inf_all, n1, n2) * 100
    if count==0:
        line = ax.plot(alpha_inf_all, pi_curr, label=r'$n_1=%d ~\rightarrow~ n_2=%d$' % (n1, n2), zorder=3)
    else:
        line = ax.plot(alpha_inf_all, pi_curr, label=r'$n_1=%d \rightarrow n_2=%d$' % (n1, n2), zorder=3)
        
    lines.append(line[0])

ax.vlines(1.0, -30, 0.0, colors='k', linestyle='--', zorder=2)

ax.set_yticks(np.arange(-30, 0.0+1, 1), minor=True)
ax.set_yticks(np.arange(-30, 0.0+5, 5), major=True)

ax.set_ylim((-30, 0))
ax.set_xscale('log')
ax.set_xticks(alpha_inf_all_lab, minor=True)
ax.set_xticks(alpha_inf_all_lab_major, major=True)
ax.set_xticklabels(alpha_inf_all_lab_major)

ax.legend(handles=lines)
ax.grid(linestyle='-', lw=1.5, which='major', color='0.8', zorder=1, axis='y')
ax.grid(linestyle='-', lw=1.5, which='both', color='0.8', zorder=1, axis='x')

ax.set_xlabel(r'$\alpha_\infty$', fontsize=12)
ax.set_ylabel(r'% change in $E[\mathrm{MSE}]$', fontsize=12)

fig.subplots_adjust(left=0.12, bottom=0.12, top=0.98, right=0.98)

if save_figs:
    plt.savefig(figdir + 'Figure3.png', dpi=500)
