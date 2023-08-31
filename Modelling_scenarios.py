#This one is the same as Modelling_complex.ipynb, but it's being used to try different scenarios

import matplotlib.pyplot as plt
import numpy as np

import pygimli as pg
import pygimli.meshtools as mt
from pygimli.physics import ert

world = mt.createWorld(start=(-350, -250), end=(350, 0))

iPos = (-80, -50) #Inyection Point
fault = mt.createPolygon([iPos, (-145, -250)], isClosed= True)

layer = mt.createPolygon([(-100, -0), iPos, (50, -50), (100, -0)], 
                         addNodes=50, interpolate='spline', isClosed=False)

world += layer
world += fault

world.addRegionMarker((0, -5), marker=1)
world.addRegionMarker((-300, -200), marker=2)
world.addRegionMarker((300, -200), marker=3)

pg.show(world, markers=True, showNodes=True)

# Sensors should no be on the corner so we put them a little inside
scheme = ert.createData(elecs=np.linspace(start=-100, stop=100, num=64),
                           schemeName='slm')

# we need local refinement at the electrodes to achieve sufficient accuracy
for p in scheme.sensors():
    world.createNode(p)
    world.createNode(p - [0, 0.1])

mesh = mt.createMesh(world)

mesh = mt.appendTriangleBoundary(mesh, xbound=200, ybound=200, marker=4)

pg.show(mesh, markers=True, showMesh=True)

rhoMin = 1
rhoMax = 100
rho0 = pg.solver.cellValues(mesh, {1: 100,
                                   2: 150,
                                   3: 500,
                                   4: 100,}
                                   )

pg.show(mesh, rho0, label='rho background', showMesh=True)

data = ert.simulate(mesh, scheme=scheme, res=rho0, 
                    noiseLevel=3, noiseAbs=1e-6, seed=1337)

pg.show(data)

#Anisotropic flow
diff = pg.solver.cellValues(mesh, {'3,2,4': pg.solver.createAnisotropyMatrix(0.1, 0.1, 0.0), 1: pg.solver.createAnisotropyMatrix(1, 100, 20.0*np.pi/180)}) 

#Isotropic and homogeneous flow
#diff = pg.solver.cellValues(mesh, {4: 1e-2, 3: 1e-2, 2: 1e-2, 1: 100}) 

iPosID = mesh.findNearestNode(iPos)

# stationary solution 
Conc = pg.solver.solve(mesh, a=diff,
                    bc={'Dirichlet': {'-1': 0.0}, 'Neumann': {'-2': -1},
                        'Node':[iPosID, 100]}, verbose=True)

pg.show(mesh, Conc, label='concentration', showMesh=True, 
        cMin=0, cMax=100, nCols=10, nLevs=11, linewidths=0.5)

Conc = pg.interpolate(mesh, Conc, mesh.cellCenters())
Conc[Conc < 0] = 0

# add anomal resistivity as linear function from rhoMin to rhoMax depending on concentration
rho = 1/(1/np.array(rho0) + 1/(rhoMin)*(Conc/100))


data = ert.simulate(mesh, scheme=scheme, res=rho, noiseLevel=3,
                    noiseAbs=1e-6, seed=1337)


data.remove(data['rhoa'] < 0)
pg.info('Filtered rhoa (min/max)', min(data['rhoa']), max(data['rhoa']))

# You can save the data for further use
data.save('Forward_mod.dat')

# You can take a look at the data
ert.show(data)

mgr = ert.ERTManager('Forward_mod.dat')

inv = mgr.invert(lam=30, verbose=True)
#np.testing.assert_approx_equal(mgr.inv.chi2(), 1, significant=1)

mgr.showResultAndFit()
meshPD = pg.Mesh(mgr.paraDomain) # Save copy of para mesh for plotting later