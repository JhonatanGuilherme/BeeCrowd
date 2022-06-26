using System;

class MainClass {
  public static void Main (string[] args) {
    string[] A = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
    int B = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine(A[B - 1]);
  }
}