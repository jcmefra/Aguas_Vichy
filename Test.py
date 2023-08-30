import numpy as np
import pygimli as pg

import pygimli.meshtools as mt
from pygimli.physics import ert

world = mt.createWorld(start=(-350, -250), end=(350, 0))

iPos = (-120, -200)
layer = mt.createPolygon([(-350, -150), iPos, (350, -150)], 
                        addNodes=100, interpolate='spline', boundaryMarker=5)

cut = mt.createPolygon([iPos, (-180, -250)])

world += layer
world += cut

world.addRegionMarker((300, -10), marker=2, area=500)

# Sensors should no be on the corner so we put them a little inside
scheme = ert.createData(elecs=np.linspace(start=-330, stop=330, num=96),
                           schemeName='slm')

# we need local refinement at the electrodes to achieve sufficient accuracy
for p in scheme.sensors():
    world.createNode(p)
    world.createNode(p - [0, 0.1])

pg.show(world, markers=True, showNodes=True)

mesh = mt.createMesh(world, quality=33, area=100)

# we need larger boundary to avoid numerical issues
mesh = mt.appendTriangleBoundary(mesh, xbound=1000, ybound=500, marker=3)
# Note. appendTriangleBoundary is just an easy fallback. You will get better results if you create the boundary manually on geometry level.


pg.show(mesh, markers=True, showMesh=True)

rhoMin = 2
rhoMax = 200
rho0 = pg.solver.cellValues(mesh, {0: 500,
                                   1: rhoMin,
                                   2: rhoMax,
                                   3: 100,}
                                   )

pg.show(mesh, rho0, label='rho background', showMesh=True)

# we simulate the ert with our forward mesh
data = ert.simulate(mesh, scheme=scheme, res=rho0, 
                    noiseLevel=3, noiseAbs=1e-6, seed=1337)

pg.show(data)

diff = pg.solver.cellValues(mesh, {'0,1,3': pg.solver.createAnisotropyMatrix(0.1, 0.1, 0.0),
                                   2: pg.solver.createAnisotropyMatrix(1, 100, 20.0*np.pi/180)}
                                   )

iPosID = mesh.findNearestNode(iPos)

# stationary solution 
C = pg.solver.solve(mesh, a=diff,
                    bc={'Dirichlet': {'-1': 0.0}, 'Neumann': {'-2': -1},
                        'Node':[iPosID, 100]}, verbose=True)

pg.show(mesh, C, label='concentration', showMesh=True, 
        cMin=0, cMax=100, nCols=10, nLevs=11, linewidths=0.5)


C = pg.interpolate(mesh, C, mesh.cellCenters())
C[C < 0] = 0

# add anomal resistivity as linear function from rhoMin to rhoMax depending on concentration
rho = 1/(1/np.array(rho0) + 1/(rhoMin)*(C/100))

data = ert.simulate(mesh, scheme=scheme, res=rho, 
                    noiseLevel=3, noiseAbs=1e-6, seed=1337)

pg.show(data)
