using System;

class MainClass {
  public static void Main (string[] args) {
    string[] S = Console.ReadLine().Split();
    int A = Convert.ToInt32(S[0]);
    int B = Convert.ToInt32(S[1]);
    int C;
    if (A < B)
      C = B - A;
    else
      C = 24 - A + B;
    Console.WriteLine("O JOGO DUROU " + C + " HORA(S)");
  }
}