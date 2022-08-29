# pip install stockfish for python wrapper

#get system info
import psutil
import math

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

from stockfish import Stockfish

path = "/home/anton/Projects/stockfish_15_win_x64_avx2/stockfish_15_src/src/stockfish"
