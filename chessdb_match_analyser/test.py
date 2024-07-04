import requests
import chess
import chess.pgn
import tools

api_url = 'http://www.chessdb.cn/cdb.php'
command = '?action=queryscore&learn=1&showall=1&board='
filepath = 'match.pgn'


evals = []

chess_pgn = open(filepath)
chess_pgn = chess.pgn.read_game(chess_pgn)

board = chess.Board()

for move in chess_pgn.mainline_moves():
    fen = str(board.fen())
    print(f"{fen} ::: detected side: {tools.getSideToMoveFromFEN(fen)}")
    board.push(move)
