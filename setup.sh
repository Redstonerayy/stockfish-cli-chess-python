git clone https://github.com/official-stockfish/Stockfish.git
cd Stockfish/src/
make net
make -j profile-build ARCH=x86-64-avx2 COMP=clang COMPCXX=clang++
cd ../../
python main.py