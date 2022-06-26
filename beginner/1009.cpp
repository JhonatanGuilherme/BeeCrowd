#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  string nome;
  double salarioFixo, totalVendas;
  cin >> nome >> salarioFixo >> totalVendas;
  cout << fixed << setprecision(2);
  cout << "TOTAL = R$ " << salarioFixo + (totalVendas * 0.15) << endl;

  return 0;
}
