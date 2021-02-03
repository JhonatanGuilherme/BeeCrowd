using System;

class URI {
  public static void Main (string[] args) {
    string[] S1 = Console.ReadLine().Split();
    string[] S2 = Console.ReadLine().Split();
    string[] S3 = Console.ReadLine().Split();
    string[] S4 = Console.ReadLine().Split();

    int D = int.Parse(S3[1]) - int.Parse(S1[1]);
    int H = int.Parse(S4[0]) - int.Parse(S2[0]);
    if (H < 0){
        H += 24;
        D --;}
    
    int M = int.Parse(S4[2]) - int.Parse(S2[2]);
    if (M < 0){
        M += 60;
        H --;}
    
    int S = int.Parse(S4[4]) - int.Parse(S2[4]);
    if (S < 0){
        S += 60;
        M --;}
    if (D <= 0){
        D = 0;}

    Console.WriteLine("{0} dia(s)\n{1} hora(s)\n{2} minuto(s)\n{3} segundo(s)", D, H, M, S);
  }
}