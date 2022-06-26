using System;

class URI {
  public static void Main (string[] args) {
    string A = Console.ReadLine();
    double B = double.Parse(Console.ReadLine());
    double C = double.Parse(Console.ReadLine());
    Console.WriteLine("TOTAL = R$ " + Math.Round((B + C * 0.15), 2).ToString("0.00"));
  }
}