using System;

class MainClass {
  public static void Main (string[] args) {
    string[] S = Console.ReadLine().Split();
		double A = double.Parse(S[0]);
		double B = double.Parse(S[1]);
		double C = double.Parse(S[2]);
		if ((A + B > C) && (A + C > B) && (C + B > A))
			Console.WriteLine("Perimetro = " + (A + B + C).ToString("0.0"));	
		else
      Console.WriteLine("Area = " + (((A + B) * C) / 2).ToString("0.0"));
  }
}