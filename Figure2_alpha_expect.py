#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:02:48 2024

@author: ard000
"""

import matplotlib.pyplot as plt
import numpy as np
from labelines import labelLines as label_lines

save_figs = False
figdir = 'path/to/figure'

Nens_all = np.arange(5, 75+1, 1)
alpha_inf_1 = np.around(np.arange(0.2, 1.0+0.1, 0.1),1)
alpha_inf_2 = np.around(np.arange(1.5, 5.0+0.5, 0.5),1)
alpha_inf_all = np.array([alpha_inf_1,alpha_inf_2],dtype=object)

def alpha_star_func(n, alpha):
    return (1.0 + n * alpha) / (n + 1)

fig = plt.figure(num=1, figsize=(8, 3.5))
plt.clf()
fig.subplots_adjust(left=0.09, top=0.92, bottom=0.14, right=0.98, wspace=0.23)

for count, alpha_inf in enumerate(alpha_inf_all):

    N, A = np.meshgrid(Nens_all, alpha_inf)
    
    alpha_star = (1.0 + N * A) / (N + 1)
    
    min_ = alpha_inf.min()
    max_ = alpha_inf.max()


    ax = fig.add_subplot(1,2,count+1)
    lw = 2.0
    l1 = ax.plot(Nens_all, alpha_star.T, lw=lw, color='k', ls='-', label=np.around(alpha_inf,1))    
    
    if count==0:
        ax.set_yticks(np.arange(min_, max_+0.05, 0.05), minor=True)
        ax.set_yticks(np.arange(min_, max_+0.1, 0.1))
        ax.set_title('Overdispersive & Consistent')
        ax.set_ylim((min_-0.02, max_+0.05))
    else:
        ax.set_yticks(np.arange(min_, max_+0.25, 0.25), minor=True)
        ax.set_yticks(np.arange(min_, max_+0.5, 0.5)) 
        ax.set_ylim((min_-0.2, max_+0.1))
        ax.set_title('Underdispersive')
        
    ax.set_xlabel('Ensemble size', fontsize=12)
    
    ax.set_ylabel(r'$\lim_{T\to\infty}~E[\alpha]$', fontsize=12, )
    ax.set_xticks(np.arange(0, Nens_all.max() + 5, 5), minor=True)
    ax.set_xticks(np.arange(0, Nens_all.max() + 10, 10))
    ax.set_xlim((5, Nens_all.max()))
    
    # x positions in plot contours for labels
    xpos1 = [50, 60] * np.ceil(len(alpha_inf)/2.).astype(int)
    label_lines(l1, xvals=xpos1, fontsize=9)
    ax.grid(linestyle='-', lw=1.5, which='major', color='0.8')

if save_figs:
    plt.savefig(figdir + 'Figure2.png', dpi=500)

