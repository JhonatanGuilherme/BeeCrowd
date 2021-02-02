#include <stdio.h>
 
int main() {
 
    int L = 0, R = 1;
    scanf("%d", &L);

    while (L >= 2) {
        L /= 2;
        R *= 4;
    }

    printf("%d\n", R);
 
    return 0;
}