using System;

class URI {
  public static void Main (string[] args) {
    int N = int.Parse(Console.ReadLine());
    int A = N / 3600;
    N %= 3600;
    int B = N / 60;
    N %= 60;
    Console.WriteLine(A + ":" + B + ":" + N);
  }
}