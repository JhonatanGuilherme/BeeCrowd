using System;

class MainClass {
  public static void Main (string[] args) {
    string[] A = Console.ReadLine().Split();
    string[] B = Console.ReadLine().Split();
    double X = Math.Pow(double.Parse(B[0]) - double.Parse(A[0]), 2);
    double Y = Math.Pow(double.Parse(B[1]) - double.Parse(A[1]), 2);
    Console.WriteLine(Math.Round(Math.Sqrt(X + Y), 4).ToString("0.0000"));
  }
}