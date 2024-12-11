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

MSE_inf = 1.0

beta1 = np.around(np.arange(MSE_inf/2, MSE_inf, MSE_inf*0.1),1)
beta2 = np.around(np.arange(MSE_inf, MSE_inf*2.0 + MSE_inf*0.1, MSE_inf*0.2),1)
beta_all = np.array([beta2,beta1],dtype=object)

sigma_e_sq_all = beta_all / MSE_inf


def alpha_star_func(n, alpha):
    return (1.0 + n * alpha) / (n + 1)


fig = plt.figure(num=1, figsize=(8, 3.5))
plt.clf()
fig.subplots_adjust(left=0.09, top=0.92, bottom=0.14, right=0.98, wspace=0.23)

for count, sigma_e_sq in enumerate(sigma_e_sq_all):

    delta_true = sigma_e_sq - MSE_inf
    N, S = np.meshgrid(Nens_all, sigma_e_sq)
    
    
    D = S - (MSE_inf + S/N)
    
    min_ = D.min()
    max_ = D.max()


    ax = fig.add_subplot(1,2,count+1)
    lw = 2.0
    l1 = ax.plot(Nens_all, D.T, lw=lw, color='k', ls='-', label=np.around(delta_true,1))    
    
    if count==0:
        ax.set_title('Overdispersive & Consistent')
    else:
        ax.set_title('Underdispersive')
        
    ax.set_xlabel('Ensemble size', fontsize=12)
    
    ax.set_ylabel('$E[\delta]$', fontsize=12)
    ax.set_xticks(np.arange(0, Nens_all.max() + 5, 5), minor=True)
    ax.set_xticks(np.arange(0, Nens_all.max() + 10, 10))
    ax.set_xlim((5, Nens_all.max()))
    
    # x positions in plot contours for labels
    xpos1 = [50, 60] * np.ceil(len(delta_true)/2.).astype(int)
    label_lines(l1, xvals=xpos1, fontsize=9)
    ax.grid(linestyle='-', lw=1.5, which='major', color='0.8')


if save_figs:
    plt.savefig(figdir + 'Figure1.png', dpi=500)

