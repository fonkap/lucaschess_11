import partida_test_data as td
from Code import VarGen
import os
import sys
sys.path.append(os.path.join('..', VarGen.folder_engines, "_tools"))
from Code import Partida
from Code import Jugada
from Code import XMotorRespuesta
from Code import ControlPosicion


j = Jugada.Jugada()
rm = XMotorRespuesta.MRespuestaMotor('McBrain', True)
rm.dicDepth[1] = {'a2a4': 183}
j.analisis = (rm, 0)
p1 = ControlPosicion.ControlPosicion()
p1.leeFen('r4rk1/pp1bqppp/1n1p1n2/2pP4/4P3/2P2PN1/P3B1PP/R1BQ1RK1 w - - 5 5')
p2 = ControlPosicion.ControlPosicion()
p2.leeFen('r4rk1/pp1bqppp/1n1p1n2/2pP4/P3P3/2P2PN1/4B1PP/R1BQ1RK1 b - a3 0 5')
j.ponDatos(p1, p2, 'a2', 'a4', '')
jugada_str = j.guardaEnTexto()
j.recuperaDeTexto(jugada_str)

jugada_str = td.jugada_bytes.decode("latin1")
j = Jugada.Jugada()
j.recuperaDeTexto(jugada_str)

partida_str = td.partida_bytes.decode("latin1")
p = Partida.Partida()
p.recuperaDeTexto(partida_str)
