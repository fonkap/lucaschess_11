from Code import VarGen
import os
import sys

sys.path.append(os.path.join('..', VarGen.folder_engines, "_tools"))
import LCEngineV1 as LCEngine

posA1 = LCEngine.posA1
a1Pos = LCEngine.a1Pos
pv2xpv = LCEngine.pv2xpv
xpv2pv = LCEngine.xpv2pv
xpv2pgn = LCEngine.xpv2pgn
PGNreader = LCEngine.PGNreader
setFen = LCEngine.setFen
makeMove = LCEngine.makeMove
getFen = LCEngine.getFen
getExMoves = LCEngine.getExMoves
fen2fenM2 = LCEngine.fen2fenM2
makePV = LCEngine.makePV
num2move = LCEngine.num2move
move2num = LCEngine.move2num

assert a1Pos('a1') == 0
assert a1Pos('b2') == 9
assert a1Pos('h8') == 63

assert posA1(0) == 'a1'
assert posA1(9) == 'b2'
assert posA1(63) == 'h8'

pv = 'd2d4 g8f6 g1f3 d7d5 e2e3 e7e6 f1d3 c7c5 c2c3 b7b6 e1g1 c8b7 b1d2 f8e7 b2b3 e8g8 c1b2 b8d7 d1e2 e7d6 c3c4 c5d4 e3d4 d8e7 f3e5 d6a3 b2a3 e7a3 f2f4 a3b2 e5f3 d5c4 b3c4 b7f3 d2f3 b2e2 d3e2 a8c8 a2a4 c8c7 a4a5 f8d8 a5b6 d7b6 f1c1 b6c8 g2g3 c8e7 a1a4 e7c6 c4c5 f6d5 f3e5 d5e7 c1c4 c6e5 f4e5 f7f6 e5f6 g7f6 e2f3 e6e5 d4e5 f6e5 c5c6 e7f5 a4a5 d8e8 c4c5 f5d4 f3e4 g8f7 g1g2 f7f6 a5a2 f6e6 c5a5 e8e7 a2f2 e7g7 h2h4 h7h5 g2h2 a7a6 e4d5 e6e7 a5a6 e7d6 d5g2 g7e7 a6a5 d4c6 f2f6 e7e6 a5d5 d6e7 f6f5 e5e4 f5h5 e4e3 h5h7 e7e8 h7c7 e3e2 g2f3 e2e1q f3h5 e8f8 d5f5 f8g8 h5f7 g8h8 f5h5 h8g7 f7e6 g7f6 h5h6 f6e5 e6h3 e1d2 h3g2 d2h6 c7c6 h6h7 c6c4 e5f6 c4g4 h7d7 g4g5'
xpv = pv2xpv(pv)
expv = 'EUxg@Om]FNnf?Ml\\DLkc>@tk;EwnCKvx<Csm=FneLT\\UNUunO^eJCJnJGWJC^O]TKTkOEOCFMFrtBRtlRZwuZcmc?<ctHPtn:RndT\\g]O^]n<Td^W^og^gpgFOf^U^g^\\dn_RZuvT\\_UOVxo@HogZBgf\\ZvnBGnpIYqaHIjbV]fnZbne]HpnbZUdGgnfZ]eng_^V_aVNaqnvqlNFHOF>2Oavw]_wxaoxy_aypofpgaig^fQ>EQHEildiqdT^gTXqmX`'
assert xpv == expv

lipv = LCEngine.xpv2lipv('EUxg')
assert lipv == ['d2d4', 'g8f6']

pv_ = LCEngine.xpv2pv(expv)
assert pv_ == pv

