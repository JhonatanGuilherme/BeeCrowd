using System;

class URI {
  public static void Main (string[] args) {
    string[] V = Console.ReadLine().Split(' ');

    double A = double.Parse(V[0]);
    double B = double.Parse(V[1]);
    double C = double.Parse(V[2]);

    double DT = Math.Pow(B, 2.0) - 4 * A* C;
    double R1 = (-B + Math.Sqrt(DT)) / (2.0 * A);
    double R2 = (-B - Math.Sqrt(DT)) / (2.0 * A);

    if (A == 0 || DT < 0.0) {
      Console.WriteLine("Impossivel calcular");
    } else {  
      Console.WriteLine("R1 = " + R1.ToString("0.00000"));
      Console.WriteLine("R2 = " + R2.ToString("0.00000"));
	  }
  }
}