#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int number, hours;
  float salary;

  cin >> number >> hours >> salary;
  cout << "NUMBER = " << number << endl;
  cout << fixed << setprecision(2);
  cout << "SALARY = U$ " << hours * salary << endl;

  return 0;
}
