#include <stdio.h>
 
int main() {
 
    int N = 0;

    while (1) {
        
        if (scanf("%d", &N) == EOF) break;

        if (N == 0)
            printf("vai ter copa!\n");
        else
            printf("vai ter duas!\n");

    }
 
    return 0;
}