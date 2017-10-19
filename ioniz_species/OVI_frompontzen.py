import matplotlib.pyplot as plt
import numpy as np
import pynbody

@pynbody.derived_array
def rhoOVI(f):
    ovi = pynbody.analysis.ionfrac.calculate(f,ion='ovi',mode='new')
    return f.gas['rho']*ovi*f.gas['OxMassFrac']
    
i = 5
sim = ['/nobackupp8/fgoverna/pioneer50h243.1536g1bwK1BH/pioneer50h243.1536gst1bwK1BH.004096','/nobackupp8/fgoverna/pioneer50h243GM1.1536gs1bwK1BH/pioneer50h243GM1.1536gst1bwK1BH.004096','/nobackupp8/fgoverna/pioneer50h243GM4.1536gst1bwK1BH/pioneer50h243GM4.1536gst1bwK1BH.004096','/nobackup/nnsanche/pioneer50h243GM5.1536gst1bwK1BH/pioneer50h243GM5.1536gst1bwK1BH.004096','/nobackupp8/fgoverna/pioneer50h243GM6.1536gst1bwK1BH/pioneer50h243GM6.1536gst1bwK1BH.004096','/nobackup/nnsanche/pioneer50h243GM7.1536gst1bwK1BH/pioneer50h243GM7.1536gst1bwK1BH.004096']
labels = ['P0','GM1','GM4','GM5','GM6','GM7']

f = pynbody.load(sim[i])

pynbody.analysis.halo.center(f.star)

f.physical_units()

pynbody.plot.sph.image(f.gas,qty='rhoOVI',width='500 kpc',units="16 m_p cm^-2",vmin=1e13,vmax=1e15,cmap='magma')
plt.savefig('GM7_OVI.pdf')
plt.show()
