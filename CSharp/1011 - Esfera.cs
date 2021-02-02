using System;

class MainClass {
  public static void Main (string[] args) {
    double A = double.Parse(Console.ReadLine());
    Console.WriteLine("VOLUME = " + Math.Round((4.0 / 3.0) * 3.14159 * Math.Pow(A, 3), 3).ToString("0.000"));
  }
}