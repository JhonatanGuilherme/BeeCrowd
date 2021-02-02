#include <stdio.h>
 
int main() {
 
    float imposto = 0, salario = 0;
  scanf("%f", &salario);

  if (salario <= 2000.00)
    printf("Isento\n");
  else {
    salario -= 2000.00;
    if (salario <= 1000.00)
      imposto += salario * 0.08;
    else if (salario <= 2500.00) {
      salario -= 1000.00;
      imposto += 1000 * 0.08 + salario * 0.18;
    }
    else {
      salario -= 2500.00;
      imposto += 1000 * 0.08 + 1500.00 * 0.18 + salario * 0.28;
    }
    printf("R$ %.2f\n", imposto);
  }
 
    return 0;
}