using System;
					
class MainClass {
	public static void Main (string[] args) {
		string[] S = Console.ReadLine().Split();
		double X = double.Parse(S[0]);
    double Y = double.Parse(S[1]);
		if (X == 0.0 && Y == 0.0) 
		  Console.WriteLine("Origem");
		else if (X > 0.0  && Y > 0.0)
		  Console.WriteLine("Q1");
		else if (X < 0.0 && Y > 0.0)
		  Console.WriteLine("Q2");
		else if (X < 0.0 && Y < 0.0)
		  Console.WriteLine("Q3");
		else if (X > 0.0 && Y < 0.0)
		  Console.WriteLine("Q4");
    else if (X == 0.0)
      Console.WriteLine("Eixo Y");
    else if (Y == 0.0)
      Console.WriteLine("Eixo X");
	}
}