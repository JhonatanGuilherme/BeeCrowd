#include <stdio.h>
 
int main() {
  int tempoGasto, velocidadeMedia;
  scanf("%d %d", &tempoGasto, &velocidadeMedia);
  printf("%.3f\n", (tempoGasto * velocidadeMedia) / 12.0);

  return 0;
}
