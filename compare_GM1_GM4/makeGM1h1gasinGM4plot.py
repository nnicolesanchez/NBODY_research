# This script makes some plots

import matplotlib.pyplot as plt
import numpy as np

new_GM4_gaspos  = np.loadtxt('GM4_GM1matchedgas_posxyz.txt')
new_GM4_gastemp = np.loadtxt('GM4_GM1matchedgas_temp.txt')
new_GM4_gasmetal = np.loadtxt('GM4_GM1matchedgas_metal.txt')

new_GM1_gaspos  = np.loadtxt('GM1matchedgas_posxyz.txt')
new_GM1_gastemp = np.loadtxt('GM1matchedgas_temp.txt')
new_GM1_gasmetal = np.loadtxt('GM1matchedgas_metal.txt')

print('Min gas temp',min(new_GM4_gastemp),'Max gas temp',max(new_GM4_gastemp))
print('# of Gas particles w/ T < 10^4 K',len(new_GM4_gastemp[new_GM4_gastemp < 10**4]))
print('# of Gas particles w/ T > 10^6 K',len(new_GM4_gastemp[new_GM4_gastemp > 10**6]))
print('% of Gas particles left out of range',str.format('{0:0.3f}',float(len(new_GM4_gastemp[new_GM4_gastemp < 10**4])+len(new_GM4_gastemp[new_GM4_gastemp > 10**6]))/len(new_GM4_gastemp)*100),'%')


#(6914.79296875, 47352908.0)
plt.scatter(new_GM4_gaspos[:,0],new_GM4_gaspos[:,1],c=np.log10(new_GM4_gastemp),s=10,cmap=plt.cm.get_cmap('jet'),alpha=0.5,vmin=4,vmax=6)
plt.title('GM4 Gas Particles (Matched with GM1 Gas)')
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.ylim(-2500,1500)
plt.xlim(-3000,2000)
cbar = plt.colorbar()
cbar.ax.set_ylabel('Temperature [log(K)]')
plt.savefig('GM4_xy_T.pdf')
plt.show()

print('Min gas metallicity',min(new_GM4_gasmetal),'Max gas metallicity',max(new_GM4_gasmetal))
print('# of Gas particles w/ Z < -2 K',len(new_GM4_gasmetal[new_GM4_gasmetal < -2]))
print('# of Gas particles w/ Z > 1 K',len(new_GM4_gasmetal[new_GM4_gasmetal > 1]))
print('Mean Z',np.mean(new_GM4_gasmetal))

plt.scatter(new_GM4_gaspos[:,0],new_GM4_gaspos[:,1],c=new_GM4_gasmetal,s=10,cmap=plt.cm.get_cmap('jet'),alpha=0.5,vmin=-2,vmax=1)
plt.title('GM4 Gas Particles (Matched with GM1 Gas)')
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.ylim(-2500,1500)
plt.xlim(-3000,2000)
cbar = plt.colorbar()
cbar.ax.set_ylabel('Metallicity')
plt.savefig('GM4_xy_Z.pdf')
plt.show()

#### GM1

print('Min gas temp',min(new_GM1_gastemp),'Max gas temp',max(new_GM1_gastemp))
print('# of Gas particles w/ T < 10^4 K',len(new_GM1_gastemp[new_GM1_gastemp < 10**4]))
print('# of Gas particles w/ T > 10^6 K',len(new_GM1_gastemp[new_GM1_gastemp > 10**6]))
print('% of Gas particles left out of range',str.format('{0:0.3f}',float(len(new_GM1_gastemp[new_GM1_gastemp < 10**4])+len(new_GM1_gastemp[new_GM1_gastemp > 10**6]))/len(new_GM1_gastemp)*100),'%')

plt.scatter(new_GM1_gaspos[:,0],new_GM1_gaspos[:,1],c=np.log10(new_GM1_gastemp),s=10,cmap=plt.cm.get_cmap('jet'),alpha=0.5,vmin=4,vmax=6)
plt.title('GM1 Gas Particles (Matched with GM4 Gas)')
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.ylim(-2500,1500)
plt.xlim(-3000,2000)
cbar = plt.colorbar()
cbar.ax.set_ylabel('Temperature [log(K)]')
plt.savefig('GM1_xy_T.pdf')
plt.show()

print('Min gas metallicity',min(new_GM1_gasmetal),'Max gas metallicity',max(new_GM1_gasmetal))
print('# of Gas particles w/ Z < -2',len(new_GM1_gasmetal[new_GM1_gasmetal < -2]))
print('# of Gas particles w/ Z > 1 K',len(new_GM1_gasmetal[new_GM1_gasmetal > 1]))
print('Mean Z',np.mean(new_GM1_gasmetal))

plt.scatter(new_GM1_gaspos[:,0],new_GM1_gaspos[:,1],c=new_GM1_gasmetal,s=10,cmap=plt.cm.get_cmap('jet'),alpha=0.5,vmin=-2,vmax=1)
plt.title('GM1 Gas Particles (Matched with GM4 Gas)')
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.ylim(-2500,1500)
plt.xlim(-3000,2000)
cbar = plt.colorbar()
cbar.ax.set_ylabel('Metallicity')
plt.savefig('GM1_xy_Z.pdf')
plt.show()
