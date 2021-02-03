using System;

class MainClass {
  public static void Main (string[] args) {
    string[] S = Console.ReadLine().Split();
    int A = int.Parse(S[0]);
    int B = int.Parse(S[1]);
    int C = int.Parse(S[2]);
    if (A >= B && A >= C)
      Console.WriteLine(A + " eh o maior");
    else if (B >= A && B >= C)
      Console.WriteLine(B + " eh o maior");
    else if (C >= A && C >= B)
      Console.WriteLine(C + " eh o maior");
  }
}