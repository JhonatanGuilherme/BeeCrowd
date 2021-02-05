#include <stdio.h>
#include <stdlib.h>

int main(void) {
  double pi = 3.14159, raio, resultado;
  scanf("%lf", &raio);
  resultado = pi * (raio * raio);
  printf("A=%.4f\n", resultado);

  return 0;
}
