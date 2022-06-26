using System;

class URI {
  public static void Main (string[] args) {
    int A = int.Parse(Console.ReadLine());
    Console.WriteLine(A);
    int B = A / 100;
    A = A % 100;
    Console.WriteLine(B + " nota(s) de R$ 100,00");
    B = A / 50;
    A = A % 50;
    Console.WriteLine(B + " nota(s) de R$ 50,00");
    B = A / 20;
    A %= 20;
    Console.WriteLine(B + " nota(s) de R$ 20,00");
    B = A / 10;
    A %= 10;
    Console.WriteLine(B + " nota(s) de R$ 10,00");
    B = A / 5;
    A %= 5;
    Console.WriteLine(B + " nota(s) de R$ 5,00");
    B = A / 2;
    A %= 2;
    Console.WriteLine(B + " nota(s) de R$ 2,00");
    B = A;
    Console.WriteLine(B + " nota(s) de R$ 1,00");
  }
}