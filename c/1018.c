#include <stdio.h>

int main() {
  int notas[] = {100, 50, 20, 10, 5, 2, 1}, num;
  scanf("%d", &num);

  printf("%d\n", num);

  for (int i = 0; i < 7; i++) {
    printf("%d nota(s) de R$ %d,00\n", num / notas[i], notas[i]);
    num %= notas[i];
  }

  return 0;
}
