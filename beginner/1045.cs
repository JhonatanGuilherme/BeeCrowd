using System;

class MainClass {
  public static void Main (string[] args) {
    string[] S = Console.ReadLine().Split();
    double A = Convert.ToDouble(S[0]);
    double B = Convert.ToDouble(S[1]);
    double C = Convert.ToDouble(S[2]);
    double D;
    if (A < B){
      D = A;
      A = B;
      B = D;
    }
    if (B < C){
      D = B;
      B = C;
      C = D;
    }
    if (A < B){
      D = A;
      A = B;
      B = D;
    }
    if (A >= B + C)
      Console.WriteLine("NAO FORMA TRIANGULO");
    else if (Math.Pow(A, 2) == Math.Pow(B, 2) + Math.Pow(C, 2))
      Console.WriteLine("TRIANGULO RETANGULO");
    else if (Math.Pow(A, 2) > Math.Pow(B, 2) + Math.Pow(C, 2))
      Console.WriteLine("TRIANGULO OBTUSANGULO");
    else if (Math.Pow(A, 2) < Math.Pow(B, 2) + Math.Pow(C, 2))
      Console.WriteLine("TRIANGULO ACUTANGULO");
    if (A == B && B == C)
      Console.WriteLine("TRIANGULO EQUILATERO");
    else if (A == B || B == C)
      Console.WriteLine("TRIANGULO ISOSCELES"); 
  }
}