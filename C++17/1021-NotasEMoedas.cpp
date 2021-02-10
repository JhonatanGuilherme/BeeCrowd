#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int aux, inteiro, moedas[] = {100, 50, 25, 10, 5, 1}, notas[] = {100, 50, 20, 10, 5, 2};
  double flutuante;
  cin >> flutuante;
  inteiro = flutuante;
  aux = (flutuante * 100) - (inteiro * 100);

  cout << "NOTAS:" << endl;
  for (int i = 0; i < 6; i++) {
    cout << inteiro / notas[i] << " nota(s) de R$ " << notas[i] << ".00" << endl;
    inteiro %= notas[i];
  }

  aux += inteiro * 100;
  cout << "MOEDAS:" << endl;
  for (int i = 0; i < 6; i++) {
    cout << fixed << setprecision(2);
    cout << aux / moedas[i] << " moeda(s) de R$ " << moedas[i] / 100.0 << endl;
    aux %= moedas[i];
  }

  return 0;
}
