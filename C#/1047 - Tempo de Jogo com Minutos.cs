using System;

class MainClass {
  public static void Main (string[] args) {
    string[] S = Console.ReadLine().Split();
    int A = Convert.ToInt32(S[0]) * 60 + Convert.ToInt32(S[1]);
    int B = Convert.ToInt32(S[2]) * 60 + Convert.ToInt32(S[3]);
    int C = B - A;
    if (A >= B)
      C = 1440 - A + B;
    Console.WriteLine("O JOGO DUROU " + (C / 60) + " HORA(S) E " + (C % 60) + " MINUTO(S)"); 
  }
}