import itertools
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import figstyle

fig, ax = plt.subplots(3, 1, figsize=(3.37,6), sharex=True)
fig.subplots_adjust(hspace=0.1)

potential = pd.read_csv('single_time_scale_potential_energy.csv')
atomic_pressure = pd.read_csv('single_time_scale_atomic_pressure.csv')
molecular_pressure = pd.read_csv('single_time_scale_molecular_pressure.csv')

format = itertools.cycle(['o-', 'v-', '^-', 's-', '<-', '>-'])

methods = ['NHL', 'SIN']
schemes = ['side', 'middle', 'blitz']

Pmin = 0
Pmax = 350

ax[-1].set_xlabel('$\\Delta t$ (fs)')
for method in methods:
    for scheme in schemes:
        ax[0].errorbar(potential.dt,
                       potential.loc[:, 'U_{}_{}'.format(method, scheme)],
                       yerr = potential.loc[:, 'dU_{}_{}'.format(method, scheme)],
                       label='{}, {}'.format(method, scheme),
                       fmt=next(format))
        ax[0].set_ylabel('$\\langle U/N \\rangle$ (kJ/mol)')

for method in methods:
    for scheme in schemes:
        ax[1].errorbar(atomic_pressure.dt,
                       atomic_pressure.loc[:, 'P_{}_{}'.format(method, scheme)],
                       yerr = atomic_pressure.loc[:, 'dP_{}_{}'.format(method, scheme)],
                       label='{}, {}'.format(method, scheme),
                       fmt=next(format))
        ax[1].set_ylim(Pmin, Pmax)
        ax[1].set_ylabel('$\\langle P_\\mathrm{atom} \\rangle$ (atm)')

for method in methods:
    for scheme in schemes:
        ax[2].errorbar(molecular_pressure.dt,
                       molecular_pressure.loc[:, 'P_{}_{}'.format(method, scheme)],
                       yerr = molecular_pressure.loc[:, 'dP_{}_{}'.format(method, scheme)],
                       label='{}, {}'.format(method, scheme),
                       fmt=next(format))
        ax[2].set_ylim(Pmin, Pmax)
        ax[2].set_ylabel('$\\langle P_\\mathrm{mol} \\rangle$ (atm)')

ax[2].legend(loc='lower center', ncol=2)

plt.show()
fig.savefig('single_time_scale_coordinates')
