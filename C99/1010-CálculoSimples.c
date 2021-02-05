#include <stdio.h>

int main() {
  int peca1, num1, peca2, num2;
  float valor1, valor2;
  scanf("%d %d %f", &peca1, &num1, &valor1);
  scanf("%d %d %f", &peca2, &num2, &valor2);
  printf("VALOR A PAGAR: R$ %.2f\n", (num1 * valor1) + (num2 * valor2));

  return 0;
}
