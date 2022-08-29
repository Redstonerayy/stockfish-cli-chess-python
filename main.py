# pip install stockfish for python wrapper

#get system info
from tabnanny import check
import psutil

#convert it to GB
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            if unit != "G":
                return False
            else:
                return f"{bytes:.2f}"
        bytes /= factor

#get thread count and half of non used RAM
threads = int(psutil.cpu_count(logical=True)/2)
memory = get_size(psutil.virtual_memory().available)

# set memory to composite of 2
mb = 2
while (mb/1000) * 2 < float(memory):
    mb *= 2

print(f"Using Stockfish with {threads} threads and {mb} MB of RAM")

# chess
from stockfish import Stockfish
import random
import os

path = "./Stockfish/src/stockfish"

stockfish = Stockfish(path=path)
stockfish.update_engine_parameters({"Hash": mb, "Threads": threads})

def stockfishmove():
    move = stockfish.get_best_move_time(3000)
    stockfish.is_move_correct(move)
    stockfish.make_moves_from_current_position([move])

def checkwin():
    evaluation = stockfish.get_evaluation()
    if evaluation["type"] == "mate":
        if evaluation["value"] == 0:
            print("Checkmate! Game ended.")
            return True

def play():
    stockfish.set_position([])
    stockfishstart = 0.5 > random.random()
    boardturned = False

    print("Starting new game")
    if stockfishstart:
        print("Stockfish makes its first turn with white.")
    else:
        print("You are white. Make your turn.")

    if stockfishstart:
        stockfishmove()
        boardturned = True
    else:
        pass

    print(stockfish.get_board_visual(not boardturned))
    while True:
        move = input()
        if stockfish.is_move_correct(move):
            stockfish.make_moves_from_current_position([move])
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Stockfish makes its turn.")
            print(stockfish.get_board_visual(not boardturned))
            if checkwin(): 
                break 
            stockfishmove()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Its your turn now.")
            print(stockfish.get_board_visual(not boardturned))
            if checkwin(): 
                break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Sorry, you can't do that. Check your move.")
            print(stockfish.get_board_visual(not boardturned))
            
    
    print("I assume you lost if you played by yourself, that is the reason why there is no message for the player winning implemented.")
    input("Press enter to play a new game ...")
    os.system('cls' if os.name == 'nt' else 'clear')
    return

#start playing
while True:
    play()