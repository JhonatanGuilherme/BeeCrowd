using System;

class MainClass {
  public static void Main (string[] args) {
    string[] S = Console.ReadLine().Split();
    int A = Convert.ToInt32(S[0]);
    int B = Convert.ToInt32(S[1]);
    int C = Convert.ToInt32(S[2]);
    int D = Convert.ToInt32(S[3]);
    if (B > C && D > A && C + D > A + B && C >= 0 && D >= 0 && A % 2 == 0)
      Console.WriteLine("Valores aceitos");
    else
      Console.WriteLine("Valores nao aceitos");
  }
}