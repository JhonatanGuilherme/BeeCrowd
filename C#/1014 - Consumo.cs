using System;

class MainClass {
  public static void Main (string[] args) {
    int X = int.Parse(Console.ReadLine());
    double Y = double.Parse(Console.ReadLine());
    Console.WriteLine(Math.Round((X / Y), 3).ToString("0.000") + " km/l");
  }
}