#include <stdio.h>
 
int main() {
 
    int contAlcool = 0, contGasolina = 0, contDiesel = 0, X = 0;
    
    while (1) {
        scanf("%d", &X);
        if (X == 1)
            contAlcool ++;
        else if (X == 2)
            contGasolina ++;
        else if (X == 3)
            contDiesel ++;
        else if (X == 4)
            break;
    }

    printf("MUITO OBRIGADO\n");
    printf("Alcool: %d\n", contAlcool);
    printf("Gasolina: %d\n", contGasolina);
    printf("Diesel: %d\n", contDiesel);
 
    return 0;
}