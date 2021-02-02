#include <stdio.h>
 
int main() {
 
    int cont = 1, I, J, K, L, V = 0;
    while (1) {
        scanf("%d", &V);
        if (V == 0)
            break;
        printf("Teste %d\n", cont++);
        I = 0, J = 0, K = 0, L = 0;
        while (V != 0) {
            if (V >= 50) {
                I++;
                V -= 50;
            }
            else if (V >= 10) {
                J++;
                V -= 10;
            }
            else if (V >= 5) {
                K++;
                V -= 5;
            }
            else {
                L++;
                V--;
            }
        }
        printf("%d %d %d %d\n", I, J, K, L);
        printf("\n");
    }
 
    return 0;
}