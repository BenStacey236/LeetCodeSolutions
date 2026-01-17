// Easy Problem
// Problem 388

#include <stdio.h>
#include <stdlib.h>

int* countBits(int n, int* returnSize) {
    int numOnes;
    int* ans;
    ans = (int *) malloc(sizeof(int) * ++n);


    for(int i = 0; i < n; i++) {
        numOnes = 0;
        int tar = i;
        while(tar != 0) {
            if((tar & 1) == 1) numOnes++;
            tar = tar >> 1;
        }

        ans[i] = numOnes;
    }

    *returnSize = n;

    return ans;
}


int main(int argc, char **argv) {
    int* array;
    int num;

    if(argc != 2) {
        printf("ERROR - must provide number\n");
        return 1;
    } else {
        num = atoi(argv[1]);
    }

    array = countBits(num, array);

    for(int i = 0; i < num+1; i++) {
        printf("%d -> %d\n", i, array[i]);
    }

    free(array);

    return 0;
}
