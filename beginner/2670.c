#include <stdio.h>
 
int main() {
 
    int A1 = 0, A2 = 0, A3 = 0, T1 = 0, T2 = 0, T3 = 0;
    scanf("%d", &A1);
    scanf("%d", &A2);
    scanf("%d", &A3);
    T1 = A2 * 2 + A3 * 4;
    T2 = A1 * 2 + A3 * 2;
    T3 = A1 * 4 + A2 * 2;
    
    if (T1 <= T2 && T1 <= T3)
        printf("%d\n", T1);
    else if (T2 <= T1 && T2 <= T3)
        printf("%d\n", T2);
    else if (T3 <= T1 && T3 <= T2)
        printf("%d\n", T3);
 
    return 0;
}