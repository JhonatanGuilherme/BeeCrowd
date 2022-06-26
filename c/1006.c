#include <stdio.h>

int main() {
  double notaA, notaB, notaC;
  scanf("%lf %lf %lf", &notaA, &notaB, &notaC);
  printf("MEDIA = %.1lf\n", (notaA * 2 + notaB * 3 + notaC * 5) / 10);

  return 0;
}
