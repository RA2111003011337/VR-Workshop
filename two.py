import viz
import vizcam
import vizshape
import vizact
viz.go()
 
cam = vizcam.PivotNavigate(center=[0,1.8,0], distance=2)
sky = viz.addChild('sky_day.osgb')
cau = viz.addChild('carousel.wrl')
pole1 = viz.addChild('pole.wrl', parent=cau)
pole1.setPosition([2.5,0,0])
pole2 = viz.addChild('pole.wrl', parent=cau)
pole2.setPosition([-2.5,0,0])
pole3 = viz.addChild('pole.wrl', parent=cau)
pole3.setPosition([0,0,2.5])
pole4 = viz.addChild('pole.wrl', parent=cau)
pole4.setPosition([0,0,-2.5])
grid = vizshape.addGrid()
world_axis = vizshape.addAxes(pos=[0,0.1,0],scale=[8,8,8])

horse1 = viz.addChild('horse.wrl', parent=pole1)
horse1.setEuler([0,0,0])
horse2 = viz.addChild('horse.wrl', parent=pole2)
horse2.setEuler([180,0,0])
horse3 = viz.addChild('horse.wrl', parent=pole3)
horse3.setEuler([-90,0,0])
horse4 = viz.addChild('horse.wrl', parent=pole4)
horse4.setEuler([90,0,0])

def spin_clk():
	cau.runAction(vizact.spin(0,10,0,-20))

def spin_cclk():
    cau.runAction(vizact.spin(0,1,0,20))

vizact.onkeydown(' ',spin_clk)
vizact.onkeyup(' ',spin_cclk)