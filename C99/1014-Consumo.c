#include <stdio.h>

int main() {
  float distanciaPercorrida;
  short int combustivelGasto;
  scanf("%d", &combustivelGasto);
  scanf("%f", &distanciaPercorrida);
  printf("%.3f km/l\n", combustivelGasto / distanciaPercorrida);
}
