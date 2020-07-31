import sys
from pcbnew import *
pcb = GetBoard()

print('Start Place XYRS')
for y in range(16):
    for x in range(16):
        Ref = 'D' + str(1 + x+(y*24))
        print(Ref)
        nPart = pcb.FindModuleByReference(Ref)
        nPart.SetPosition(wxPoint(FromMM(x*2.5), FromMM(y*2.5)))  # Update XY
        nPart.SetRotation(0.45);
        

print('Finished Place XYRS, Press F11 to refresh display')

# exec(open('../../ref/leds.py').read())
