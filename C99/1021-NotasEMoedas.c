#include <stdio.h>

int main() {
  int aux, inteiro, moedas[] = {100, 50, 25, 10, 5, 1}, notas[] = {100, 50, 20, 10, 5, 2};
  double flutuante;
  scanf("%lf", &flutuante);
  inteiro = flutuante;
  aux = (flutuante * 100) - (inteiro * 100);

  printf("NOTAS:\n");
  for (int i = 0; i < 6; i++) {
    printf("%d nota(s) de R$ %d.00\n", inteiro / notas[i], notas[i]);
    inteiro %= notas[i];
  }

  aux += inteiro * 100;
  printf("MOEDAS:\n");
  for (int i = 0; i < 6; i++) {
    printf("%d moeda(s) de R$ %.2lf\n", aux / moedas[i], moedas[i] / 100.0);
    aux %= moedas[i];
  }

  return 0;
}
