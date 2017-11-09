import os
import sys
from Code import VarGen
from Code import Util
from Code import Procesador
from Code import Sonido
from Code.QT import Gui

from Code.Constantes import *
import traceback

DEBUG = True
VERSION = "11.00.21b"

if DEBUG:
    prlkn("DEBUG " * 20)

sys._excepthook = sys.excepthook
def my_exception_hook(exctype, value, tb):
    # Print the error and traceback
    print(exctype, value, tb)
    # traceback.print_tb(tb)

    # Call the normal Exception hook after
    sys._excepthook(exctype, value, tb)
    sys.exit(1)

def init():
    if DEBUG:
        sys.excepthook = my_exception_hook
    else:
        sys.stderr = Util.Log("bug.log")

    mainProcesador = Procesador.Procesador()
    mainProcesador.setVersion(VERSION)

    runSound = Sonido.RunSound()

    resp = Gui.lanzaGUI(mainProcesador)
    runSound.close()
    mainProcesador.pararMotores()
    mainProcesador.quitaKibitzers()

    if resp == kFinReinicio:
        if sys.argv[0].endswith(".py"):
            exe = os.path.abspath(sys.argv[0])
        else:
            exe = "Lucas.exe" if VarGen.isWindows else "Lucas"
        VarGen.startfile(exe)

    sys.exit(resp)
