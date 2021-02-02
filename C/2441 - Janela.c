#include <stdio.h>
#include <stdlib.h>

int cmpfunc (const void * a, const void * b) {
   return (*(int*)a - *(int*)b);
}

int main() {

    int F[3];
    int C = 400;
    scanf("%d %d %d", &F[0], &F[1], &F[2]);
    qsort(F, 3, sizeof(int), cmpfunc);

    if (F[0] + 200 >= F[1])
        C -= F[1] - F[0];
    else
        C -= 200;
    
    if (F[1] + 200 >= F[2])
        C -= F[2] - F[1];
    else
        C -= 200;

    printf("%d\n", C * 100);

    return 0;

}