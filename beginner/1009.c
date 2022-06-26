#include <stdio.h>

int main() {
  char nome[20];
  double salarioFixo, totalVendas;
  scanf("%s %lf %lf", nome, &salarioFixo, &totalVendas);
  printf("TOTAL = R$ %.2lf\n", salarioFixo + (totalVendas * 0.15));

  return 0;
}
