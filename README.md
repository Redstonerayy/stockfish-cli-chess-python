# Stockfish test
This is a developement build of the stockfish engine straight from their website.
Download nnue with `make net`
Build on Linux with clang in the stockfish_15_src/src folder via Makefile with `make -j profile-build ARCH=x86-64-avx2 COMP=clang COMPCXX=clang++`.
Clean with `objclean`.

Python code for working with Stockfish in /python