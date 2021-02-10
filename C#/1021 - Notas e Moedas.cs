using System;

class URI {
  public static void Main (string[] args) {
    double N = double.Parse(Console.ReadLine());
    int M = Convert.ToInt32(Convert.ToDouble((N % 1).ToString("0.00")) * 100);
    N -= M / 100.0;
    int A = Convert.ToInt32(N);
    int B = A / 100;
    Console.WriteLine("NOTAS:");
    Console.WriteLine(B + " nota(s) de R$ 100.00");
    A %= 100;
    B = A / 50;
    Console.WriteLine(B + " nota(s) de R$ 50.00");
    A %= 50;
    B = A / 20;
    Console.WriteLine(B + " nota(s) de R$ 20.00");
    A %= 20;
    B = A / 10;
    Console.WriteLine(B + " nota(s) de R$ 10.00");
    A %= 10;
    B = A / 5;
    Console.WriteLine(B + " nota(s) de R$ 5.00");
    A %= 5;
    B = A / 2;
    Console.WriteLine(B + " nota(s) de R$ 2.00");
    A %= 2;
    B = A / 1;
    Console.WriteLine("MOEDAS:");
    Console.WriteLine(B + " moeda(s) de R$ 1.00");
    A = M / 50;
    Console.WriteLine(A + " moeda(s) de R$ 0.50");
    M %= 50;
    A = M / 25;
    Console.WriteLine(A + " moeda(s) de R$ 0.25");
    M %= 25;
    A = M / 10;
    Console.WriteLine(A + " moeda(s) de R$ 0.10");
    M %= 10;
    A = M / 5;
    Console.WriteLine(A + " moeda(s) de R$ 0.05");
    M %= 5;
    A = M / 1;
    Console.WriteLine(A + " moeda(s) de R$ 0.01");
  }
}