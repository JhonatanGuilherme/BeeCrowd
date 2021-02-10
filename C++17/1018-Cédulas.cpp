#include <iostream>

using namespace std;

int main() {
  int notas[] = {100, 50, 20, 10, 5, 2, 1}, num;
  cin >> num;

  cout << num << endl;

  for (int i = 0; i < 7; i++) {
    cout << num / notas[i] << " nota(s) de R$ " << notas[i] << ",00" << endl;
    num %= notas[i];
  }

  return 0;
}
