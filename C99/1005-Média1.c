#include <stdio.h>

int main(void) {
  double notaA, notaB;
  scanf("%lf %lf", &notaA, &notaB);
  printf("MEDIA = %.5lf\n", ((notaA * 3.5) + (notaB * 7.5)) / 11);
  
  return 0;
}
