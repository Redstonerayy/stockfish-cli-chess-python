# Stockfish CLI Chess
Finally you can lose against one of the best Chess AIs in your terminal.<br>
On unix run the setup script `chmod +x ./setup.sh` to make it executable and then run it with `./setup.sh`.
<br>
It automates the manual build and assume you have clang and clang++ installed and your cpu has support for avx2

# Manual Build
* Install stockfish for python with `pip install stockfish`
* Clone the official repo with `git clone https://github.com/official-stockfish/Stockfish.git`
* Go into the source folder `cd Stockfish/src/`
* Download the latest neural network `make net`
* Build stockfish with the desired arguments `make {your arguments}` e.g. `make build ARCH=x86-64-modern`
* Run the game with `python main.py`.

# Note
* Only tested on Linux. May work on Unix-Like Systems (e.g. MacOs, BSD) but not tested for Windows.
* This is a simple low effort program. Just simple CLI, nothing more yet.
* If you encounter problems you may open an issue