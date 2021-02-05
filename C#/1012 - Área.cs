using System;

class URI {
  public static void Main (string[] args) {
    string[] V = Console.ReadLine().Split(' ');
	  const double PI = 3.14159;
    double A = double.Parse(V[0]);
    double B = double.Parse(V[1]);	
    double C = double.Parse(V[2]);
    double AT = (A * C) / 2;
		Console.WriteLine("TRIANGULO: " + AT.ToString("0.000"));
    double AC = PI * (C * C);
    Console.WriteLine("CIRCULO: " + AC.ToString("0.000"));
    double ATR = ((A + B) * C) / 2;
    Console.WriteLine("TRAPEZIO: " + ATR.ToString("0.000"));
    double AQ = B * B;
    Console.WriteLine("QUADRADO: " + AQ.ToString("0.000"));
    double RT = A * B;
		Console.WriteLine("RETANGULO: " + RT.ToString("0.000"));
  }
}