import itertools
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import figstyle

fig, ax = plt.subplots(1, 1, figsize=(3.37,2), sharex=True)
fig.subplots_adjust(hspace=0.1)

temperature = pd.read_csv('single_time_scale_temperature.csv')

format = itertools.cycle(['o-', 'v-', '^-', 's-', '<-', '>-'])

methods = ['NHL']
schemes = ['side', 'middle', 'blitz']

Pmin = 0
Pmax = 350

ax.set_xlabel('$\\Delta t$ (fs)')
for method in methods:
    for scheme in schemes:
        ax.errorbar(temperature.dt,
                    temperature.loc[:, 'T_{}_{}'.format(method, scheme)],
                    yerr = temperature.loc[:, 'dT_{}_{}'.format(method, scheme)],
                    label='{}, {}'.format(method, scheme),
                    fmt=next(format))
        ax.set_ylabel('$\\langle T_\\mathrm{kin} \\rangle$ (K)')

ax.legend(loc='lower left', ncol=1)

plt.show()
fig.savefig('single_time_scale_momenta')
