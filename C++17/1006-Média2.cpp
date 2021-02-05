#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  double notaA, notaB, notaC;
  cin >> notaA >> notaB >> notaC;
  cout << fixed << setprecision(1);
  cout << "MEDIA = " << ((notaA * 2) + (notaB * 3) + (notaC * 5)) / 10 << endl;

  return 0;
}