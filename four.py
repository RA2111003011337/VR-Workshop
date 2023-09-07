import viz
import vizcam
import vizshape
import vizact
viz.go()

scene = viz.addChild('piazza.osgb')
drone = viz.addChild('drone.fbx')

cam = vizcam.PivotNavigate(center=[0,1.8,0], distance=2)
drone.setScale(0.001,0.001,0.001)
world_axis = vizshape.addAxes(pos=[0,0.1,0])
drone.setPosition([0,1.8,0])
drone.setEuler([0,90,0])

spin_ck = vizact.spin(0,0,1,36)

prop1 = drone.getChild('Propeller01')
prop1.setCenter([-250,-50,0])
prop1.addAction(spin_ck)

prop3 = drone.getChild('Propeller03')
prop3.setCenter([250,450,0])
prop3.addAction(spin_ck)

prop2 = drone.getChild('Propeller02')
prop2.setCenter([-250,450,0])
prop2.addAction(spin_ck)

prop4 = drone.getChild('Propeller04')
prop4.setCenter([250,-50,0])
prop4.addAction(spin_ck)

position = [[0.,7.,5.],[5.,7.,10.],[0.,7.,17.],[-5.,7.,10.]]
my_path = viz.addAnimationPath()
for count,posi in enumerate(position):
	print(count,posi)
	cp = viz.addControlPoint(pos=posi)
	my_path.addControlPoint(count+1,cp)
	
my_path.setTranslateMode(viz.CUBIC_BEZIER)
my_path.computeTangents()
my_path.setLoopMode(viz.CIRCULAR)

my_path.play()

viz.link(my_path,drone)

''''my_view =viz.MainView
viz.link(drone, my_view)'''