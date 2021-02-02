#include <stdio.h>
 
int main() {
 
    int X = 0;
    while (1) {
        scanf("%d", &X);
        if (X == 2002)
            break;
        printf("Senha Invalida\n");
    }
    printf("Acesso Permitido\n");
 
    return 0;
}