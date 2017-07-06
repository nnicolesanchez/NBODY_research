# This script plots face-on and edge-on plots of ChaNGa Nbody
# simulations in gas density and overplots the virial radius


# N. Nicole Sanchez -- July 5, 2017
# U. W. Seattle     -- Nbody Shop
import matplotlib.pyplot as plt
#import matplotlib.cm as cm
import numpy as np
import pynbody
import sys

plt.rc('font', size=12, family='serif', style='normal', variant='normal', stretch='normal', weight='normal')
plt.rc('xtick', labelsize=12)
plt.rc('xtick.major', size=6, width=1)
plt.rc('lines', lw=2)
plt.rc('axes', lw=1, labelsize=12)

if len(sys.argv) == 1:
    print('No galaxy selected. Current options: P0, GM1, GM4')
    print('Syntax: "GM_xygasplots.py GM1"')
    quit()
else:
    if (str(sys.argv[1]) == 'P0'):
        name = str(sys.argv[1])
        sim = pynbody.load('/nobackupp8/fgoverna/pioneer50h243GM1.1536gs1bwK1BH/pioneer50h243GM1.1536gst1bwK1BH.004096')
        print('P0 simulation at z = ','%.2f' % sim.properties['z'] )
        R_vir = np.loadtxt('../P0/P0_mainhalo.stat',dtype=float,skiprows=1,usecols=6,unpack=True)
        print('Virial radius:',float(R_vir))
        R_vir = float(R_vir)

    elif (str(sys.argv[1]) == 'GM1'):
        name = str(sys.argv[1])
        sim = pynbody.load('/nobackupp8/fgoverna/pioneer50h243GM1.1536gs1bwK1BH/pioneer50h243GM1.1536gst1bwK1BH.004096')
        print('GM1 simulation at z = ','%.2f' % sim.properties['z'] )
        R_vir = np.loadtxt('../GM1/GM1_mainhalo.stat',dtype=float,skiprows=1,usecols=6,unpack=True)
        print('Virial radius:',float(R_vir))
        R_vir = float(R_vir)
        
    elif (str(sys.argv[1]) == 'GM4'):
        print('Nicole, you forgot to input the path to load GM4')
        quit()

    else :
        print('Not a valid option. Current options: P0, GM1, GM4')
        print('Syntax: "GM_xygasplots.py GM1"')
        quit()

h = sim.halos()
h1 = h[1]
pynbody.analysis.halo.center(h1,mode='ssc')
pynbody.analysis.angmom.faceon(h1)
sim.physical_units()


# Plotting face on
pynbody.plot.sph.image(sim.g, width=2*R_vir, cmap='jet', units="g cm**-2", show_cbar=False)
fig = plt.gcf()
ax = fig.gca()

circle2 = plt.Circle((0.0, 0.0), R_vir, color='white',fill=False,linestyle='--')
ax.add_artist(circle2)
cbar = plt.colorbar()
cbar.set_label(r'g cm$^{-2}$')
plt.savefig(name+'_faceon_gas.pdf')
plt.show()



# Plotting side on
pynbody.analysis.angmom.sideon(h1)

pynbody.plot.sph.image(sim.g, width=2*R_vir, cmap='jet', units="g cm**-2", show_cbar=False)
fig = plt.gcf()
ax = fig.gca()

circle2 = plt.Circle((0.0, 0.0), R_vir, color='white',fill=False,linestyle='--')
ax.add_artist(circle2)
cbar = plt.colorbar()
cbar.set_label(r'g cm$^{-2}$')
plt.savefig(name+'_faceon_gas.pdf')
plt.show()
