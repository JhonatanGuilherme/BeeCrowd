#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  float distanciaPercorrida;
  short int combustivelGasto;
  cin >> combustivelGasto >> distanciaPercorrida;
  cout << fixed << setprecision(3);
  cout << combustivelGasto / distanciaPercorrida << " km/l" << endl;
}
