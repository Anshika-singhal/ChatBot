import os

import eel

eel.init("www")

from engine.features import playAssistantSound
# from engine.features import *
from engine.command import *

eel.init("www")

playAssistantSound()
os.system('start msedge.exe --app="http://localhost:8000/index.html"')
eel.start('index.html', mode=None, host='localhost', block=True)