#include <iostream>
#include "cfiles/ndarray.h"

extern "C" int test(numpyArray<long> A, numpyArray<long> B) {
    Ndarray<long,2> matrix(A);
    Ndarray<long,2> ret_matrix(B);
    int N = matrix.getShape(0);

    for(int i = 0; i < matrix.getShape(0); i++) {
        for(int k = 0; k < matrix.getShape(1); k++) {
            std::cout << matrix[i][k] << " ";
            ret_matrix[i][k] = 888;
        }
        std::cout << '\n';
    }

    return N;
}
