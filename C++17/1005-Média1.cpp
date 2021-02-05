#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  double notaA, notaB;
  cin >> notaA >> notaB;
  cout << fixed << setprecision(5);
  cout << "MEDIA = " << ((notaA * 3.5) + (notaB * 7.5)) / 11 << endl;

  return 0;
}