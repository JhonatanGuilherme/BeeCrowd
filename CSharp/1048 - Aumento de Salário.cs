using System;

class MainClass {
  public static void Main (string[] args) {
    double A = Convert.ToDouble(Console.ReadLine());
    double B;
    int C;
    if (A <= 400.00){
      B = A * 1.15;
      C = 15;
    }
    else if (A <= 800.00){
      B = A * 1.12;
      C = 12;
    }
    else if (A <= 1200.00){
      B = A * 1.10;
      C = 10;
    }
    else if (A <= 2000.00){
      B = A * 1.07;
      C = 7;
    }
    else{
      B = A * 1.04;
      C = 4;
    }
    Console.WriteLine("Novo salario: " + B.ToString("0.00"));
    Console.WriteLine("Reajuste ganho: " + (B - A).ToString("0.00"));
    Console.WriteLine("Em percentual: " + C + " %");
  }
}