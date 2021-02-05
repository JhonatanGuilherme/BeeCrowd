#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main() {
  double raio;
  cin >> raio;
  cout << fixed << setprecision(3);
  cout << "VOLUME = " << (4.0 / 3.0) * 3.14159 * pow(raio, 3) << endl;

  return 0;
}
