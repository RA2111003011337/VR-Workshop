import viz
import vizcam
import vizshape
import vizact
viz.go()

scene = viz.addChild('piazza.osgb')
scene = vizfx.addChild('piazza.osgb')

avatar = vizfx.addAvatar('Erika Archer.osgb')
vizact.onkeydown('1',avatar.state,1)
vizact.onkeydown('2',avatar.state,2)
vizact.onkeydown('3',avatar.state,3)
vizact.onkeydown('4',avatar.state,4)
vizact.onkeydown('5',avatar.state,5)
vizact.onkeydown('6',avatar.state,6)
vizact.onkeydown('7',avatar.state,7)
vizact.onkeydown('8',avatar.state,8)
vizact.onkeydown('9',avatar.state,9)