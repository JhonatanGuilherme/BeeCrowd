#include <iostream>
#include <iomanip>

using namespace std;
 
int main() {
  int tempoGasto, velocidadeMedia;
  cin >> tempoGasto >> velocidadeMedia;
  cout << fixed << setprecision(3);
  cout << (tempoGasto * velocidadeMedia) / 12.0 << endl;

  return 0;
}
