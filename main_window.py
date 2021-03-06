import maya.cmds as cmds
# cmds.file(f=True, new=True)
sc = cmds.internalVar(userScriptDir=True)

#Fixing import issue: 
#-----------------------------------------------------------

from lib import test
from lib import canape
from lib import TableChaise
from lib import Chair
from lib import Table
from lib import library
from lib import bed
from lib import room
from lib import Comode
from lib import Lamp
from lib import armoire
from lib import armoireUp
from lib import four
from lib import tv
modules = [test, canape, TableChaise, Chair, Table, library, bed, room, Comode, Lamp, armoire, armoireUp, four, tv]

def reload_it():
  for sub_module in modules:
    print "Reloading %s" % sub_module
    reload(sub_module)


reload_it()

#--------------------------------------------------------------

backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winName = 'Main_Window'
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Forniture Generator', bgc=(backgroundColor))
# form = cmds.formLayout()
tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
# cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
#reference to the main columnLayout
mainRLWidth = [winWidth*0.4, winWidth*0.4]
child1 = cmds.rowColumnLayout(w=winWidth, numberOfColumns=4, columnWidth=[(1, 150), (2, 150), (3, 150), (4, 150)])
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/biblioteque.png', label='Room',width=mainRLWidth[1]*0.2, c='cmds.showWindow(room.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/canape.png', label='Canape',width=mainRLWidth[1]*0.2, c='cmds.showWindow(canape.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/table_chaise.png', label='Table & Chair',width=mainRLWidth[1]*0.2, c='cmds.showWindow(TableChaise.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/chaise.png', label='Chair',width=mainRLWidth[1]*0.2, c='cmds.showWindow(Chair.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/table.png', label='Table',width=mainRLWidth[1]*0.2, c='cmds.showWindow(Table.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/biblioteque.png', label='Library',width=mainRLWidth[1]*0.2, c='cmds.showWindow(library.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/lamp.png', label='Lamp',width=mainRLWidth[1]*0.2, c='cmds.showWindow(Lamp.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.setParent( '..' )
child2 = cmds.rowColumnLayout(w=winWidth, numberOfColumns=4, columnWidth=[(1, 150), (2, 150), (3, 150), (4, 150)])
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/lit.png', label='Bed',width=mainRLWidth[1]*0.2, c='cmds.showWindow(bed.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/comode.png', label='Comode',width=mainRLWidth[1]*0.2, c='cmds.showWindow(Comode.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/comode.png', label='TV',width=mainRLWidth[1]*0.2, c='cmds.showWindow(tv.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.setParent( '..' )
child3 = cmds.rowColumnLayout(w=winWidth, numberOfColumns=4, columnWidth=[(1, 150), (2, 150), (3, 150), (4, 150)])
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/1x/moduledown_cuisine.png', label='Cupboard Down',width=mainRLWidth[1]*0.2, c='cmds.showWindow(armoire.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/1x/moduleup_cuisine.png', label='Upper Cupboard',width=mainRLWidth[1]*0.2, c='cmds.showWindow(armoireUp.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/1x/moduledown_cuisine.png', label='Oven',width=mainRLWidth[1]*0.2, c='cmds.showWindow(four.winName)')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/coming_soon.png', label='Coming Soon', c='')
cmds.setParent( '..' )
cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'LIVING ROOM'), (child2, 'BED ROOM'), (child3, 'KITCHEN')), bgc=(backgroundColor))
cmds.showWindow(winName)
cmds.window(winName, e=True, width=winWidth, height=470)