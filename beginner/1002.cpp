#include <iostream>
#include <iomanip>

using namespace std;

int main(void) {
  
  double pi = 3.14159, raio, resultado;

  cin >> raio;

  resultado = pi * (raio * raio);
  cout << fixed << setprecision(4);
  cout << "A=" << resultado << endl;

  return 0;
}
