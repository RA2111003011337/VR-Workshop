import viz
import vizcam
import vizshape
import vizact
viz.go()

ground = viz.addChild('ground.osgb')
vol = viz.addChild('volleyball.osgb')
bask = viz.addChild('basketball.osgb')
soc = viz.addChild('soccerball.osgb')
arrow = viz.addChild('arrow.wrl')
arrow.setScale([0.1,0.1,0.1])
cam = vizcam.PivotNavigate(center=[0,1.8,0], distance=2)

vol.setPosition([-1,0,0])
bask.setPosition([1,0,0])

def pick_ball():
	obj = viz.pick()
	if obj.valid():
		position = obj.getPosition()
		print(position)
		arrow.color(viz.RED)
		arrow.visible(viz.ON)
		position[1]+=0.3
		arrow.setPosition(position)

vizact.onmousedown(viz.MOUSEBUTTON_LEFT,pick_ball)

bounce_up = vizact.moveTo([-1,2,0], time=1)
bounce_down = vizact.moveTo([-1,1,0], time=1)
bounce = vizact.sequence([bounce_up, bounce_down],viz.FOREVER)
spin = vizact.spin(0,1,0,-20)
soc.addAction(spin)
vol.addAction(bounce)
soc.addAction(spin)

trans_rot = viz.mergeLinkable(vol,soc)
merge_link = viz.link(trans_rot,bask)
merge_link.postTrans([2,0,0])

