#include <stdio.h>
 
int main() {
 
  double X;
  scanf("%lf", &X);

  if (X < 0.00 || X > 100.00)
    printf("Fora de intervalo\n");
  else if (X <= 25.00)
    printf("Intervalo [0,25]\n");
  else if (X <= 50.00)
    printf("Intervalo (25,50]\n");
  else if (X <= 75.00)
    printf("Intervalo (50,75]\n");
  else
    printf("Intervalo (75,100]\n");
 
    return 0;
}