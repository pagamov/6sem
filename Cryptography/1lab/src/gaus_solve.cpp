#include <iostream>
#include <vector>
#include <unordered_set>
#include "cfiles/ndarray.h"


class cBiteMatrix {
class column;
public:
    cBiteMatrix(int i): n(i), m(i) {
        data.resize(n, column(m));
        for(int i = 0; i < n; i++) {
            data[i].put(1, i);
        }
    }
    cBiteMatrix(Ndarray<long,2>& from): n(from.getShape(1)), m(from.getShape(0)) {
        data.resize(n, column(m));
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                data[i].put(from[j][i], j);
            }
        }
    }

    void addCollumnToAnother(int i, int k) {
        data[k] ^= data[i];
    }

    column operator[](int i) {

        return data[i];
    } 
private:
    class column {
    public:
        std::vector<unsigned long long> data;
        column(int i){
            if(i % 64) {
                data.resize(i / 64 + 1, 0);
            } else {
                data.resize(i / 64, 0);
            }
        }
        int operator[](int i) {
            return (data[i / 64] & (1ull << (i % 64))) ? 1 : 0;
        }
        void operator^=(const column& from) {
            for(int i = 0; i < data.size(); i++ ) {
                data[i] ^= from.data[i];
            }
        }
        void put(int a, int i) {
            if (a % 2) {
                data[i / 64] |= (1ull << (i % 64));
                
            } else {
                unsigned long long mask = 1ull << (i % 64);
                mask = ~mask;
                data[i / 64] &= mask;
            }
        }
        bool isZeroRow() {
            for(int i = 0; i < data.size(); i++) {
                if (data[i] != 0) {
                    return false;
                }
            }
            return true;
        }

        int findFirstOne(std::unordered_set<int>& banned_columns) {
            int i = 0;
            while(i < data.size()) {
                while(i < data.size()) {
                    if (data[i] == 0) {
                        i++;
                    }
                    else {
                        break;
                    }
                }
                if (i == data.size()) {
                    return -1;
                } else {
                    for(int k = 0; k < 64; k++) {
                        if(data[i] & (1ull << k)) {
                            if (banned_columns.find(i * 64 + k) == banned_columns.end())
                                return i * 64 + k;
                        }
                    }
                }
                i++;
            }
            return -1;
        }
    }; 
    int n;
    int m;
    std::vector<column> data;
};

extern "C" int test(numpyArray<long> A, numpyArray<long> B) {
    
    Ndarray<long,2> matrix_from(A);
    Ndarray<long,2> ret_matrix(B);

    int N = matrix_from.getShape(0);

    std::cout << "making bit matrix\n";

    cBiteMatrix matrix(matrix_from);

    std::cout << "making lineal columns support matrix\n";
    cBiteMatrix lineal_cols(N);

    std::unordered_set<int> banned_columns;

    std::cout << "start solving\n";
    int x;
    for(int i = 0; i < N - 1; i++) 
    {
        std::cout << "progress: " << (((float)i / N) * 100) << "\t  % \r";
        x = matrix[i].findFirstOne(banned_columns);
        banned_columns.insert(x);
        if(x >= 0) {
            for(int j = i + 1; j < N; j++) {
                if(matrix[j][x] == 1 && i != j) {
                    matrix.addCollumnToAnother(i, j);
                    lineal_cols.addCollumnToAnother(i, j);
                }
            }
        }
    }


    std::cout << "\n\nPreparing ansver\n";
    int z = 0;
    for(int i = 0; i < N; i++) {
        std::cout << "progress: " << (((float)i / N) * 100) << "\t  % \r";
        if(matrix[i].isZeroRow()) {
            for(int k = 0; k < N; k++) {
                ret_matrix[k][z] = lineal_cols[i][k];
            }
            z++;
        }
    }
    
    return z;
    // return 1;
}
