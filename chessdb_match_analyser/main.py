import requests
import chess
import chess.pgn
import tools
from time import sleep

learn = '1'

api_url = 'http://www.chessdb.cn/cdb.php'
command = '?action=queryscore&learn='+learn+'&showall=1&board='
filepath = 'match.pgn'
fileout_path = 'out.txt'
fileout = open(fileout_path, 'w')
fileepd = open("fens.epd", 'w+')






evals = []
fens = []

chess_pgn = open(filepath)
chess_pgn = chess.pgn.read_game(chess_pgn)

board = chess.Board()

allmoves = len(list(chess_pgn.mainline_moves()))
counter = 0

for move in chess_pgn.mainline_moves():
    counter+=1
    print(f"{counter} of {allmoves} positions processed")
    current_fen = str(board.fen())
    fens.append(current_fen)
    data = requests.get(api_url + command + current_fen).text
    #sleep(0.2)

    if not ('unknown' in data):
        ev = int(data[:-1].replace("eval:",""))
        if not tools.getSideToMoveFromFEN(current_fen):
            ev*=-1
        evals.append(ev/100)
    else:
        evals.append('?')
    board.push(move)


current_fen = str(board.fen())
data = requests.get(api_url + command + current_fen).text

if not ('unknown' in data):
    ev = int(data[:-1].replace("eval:",""))
    if not tools.getSideToMoveFromFEN(current_fen):
        ev*=-1
    evals.append(ev/100)
else:
    evals.append('?')


tmp = list(map(evals, str()))
#print(evals)
for i in evals:
    print(str(i).replace('.',','))
    fileout.write(str(i).replace('.',',') + '\n')

for fen in fens:
    fileepd.write(fen+"\n")
fileout.close()
fileepd.close()



#print(data)
#print(data.text)