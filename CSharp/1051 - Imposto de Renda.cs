using System;

class MainClass {
  public static void Main (string[] args) {
    double A = Convert.ToDouble(Console.ReadLine());
    if (A <= 2000.00)
      Console.WriteLine("Isento");
    else if (A <= 3000.00)
      Console.WriteLine("R$ " + ((A - 2000.00) * 0.08).ToString("0.00"));
    else if (A <= 4500.00)
      Console.WriteLine("R$ " + (1000.00 * 0.08 + (A - 3000.00) * 0.18).ToString("0.00"));
    else
      Console.WriteLine("R$ " + ((1000.00 * 0.08) + (1500.00 * 0.18) + (A - 4500.00) * 0.28).ToString("0.00"));
  }
}