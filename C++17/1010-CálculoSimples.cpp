#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int peca1, num1, peca2, num2;
  float valor1, valor2;
  cin >> peca1 >> num1 >> valor1;
  cin >> peca2 >> num2 >> valor2;
  cout << fixed << setprecision(2);
  cout << "VALOR A PAGAR: R$ " << (num1 * valor1) + (num2 * valor2) << endl;

  return 0;
}