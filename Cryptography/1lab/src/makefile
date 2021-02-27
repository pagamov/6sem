CC = g++
LD = g++
CCFLAGS = -Wall -pedantic -O3 -std=c++14
LDFLAGS =

libvector.so: gaus_solve.o
	$(LD) -shared -o gaus_solve.so gaus_solve.o

gaus_solve.o: gaus_solve.cpp cfiles/ndarray.h
	$(CC) $(CCFLAGS) -c -fPIC gaus_solve.cpp
