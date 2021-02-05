using System;

class URI {
  public static void Main (string[] args) {
    string[] A = Console.ReadLine().Split();
    string[] B = Console.ReadLine().Split();
    double C = double.Parse(A[1]) * double.Parse(A[2]);
    double D = double.Parse(B[1]) * double.Parse(B[2]);
    Console.WriteLine("VALOR A PAGAR: R$ " + Math.Round((C + D), 2).ToString("0.00"));
  }
}