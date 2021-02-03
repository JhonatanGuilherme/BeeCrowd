using System;

class MainClass {
  public static void Main (string[] args) {
    string[] S = Console.ReadLine().Split();
    int A = Convert.ToInt32(S[0]);
    int B = Convert.ToInt32(S[1]);
    if (A >= B && A % B == 0 || A < B && B % A == 0)
      Console.WriteLine("Sao Multiplos");
    else
      Console.WriteLine("Nao sao Multiplos");
  }
}