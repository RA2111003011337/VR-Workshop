import viz
import vizcam
import vizshape
import vizact
viz.go()
 
cam = vizcam.PivotNavigate(center=[0,1.8,0], distance=2)
sky = viz.addChild('sky_day.osgb')

grid = vizshape.addGrid()
#
world_axis = vizshape.addAxes(pos=[0,0.1,0])

parent_axis = vizshape.addAxes(pos=[2,0.1,3])
parent_axis.setEuler([90,0,0])

avatar = viz.addAvatar('vcc_male.cfg', parent=parent_axis)
avatar_axis =  vizshape.addAxes(pos=[0,2,0],scale=[0.3,0.3,0.3],parent=avatar)
avatar.setPosition([2,0,0],viz.REL_LOCAL)
avatar.setPosition([12,0,0],viz.ABS_GLOBAL)