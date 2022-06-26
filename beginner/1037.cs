using System;

class URI {
  public static void Main (string[] args) {
    double V = Convert.ToDouble(Console.ReadLine());
		if (V >= 0 && V <= 25)
			Console.WriteLine("Intervalo [0,25]");
		else if (V >= 25.01 && V <= 50)
		  Console.WriteLine("Intervalo (25,50]");
		else if (V >= 50.01 && V <= 75)
		  Console.WriteLine("Intervalo (50,75]");
		else if (V >= 75.01 && V <= 100)
		  Console.WriteLine("Intervalo (75,100]");
		else
		  Console.WriteLine("Fora de intervalo");
  }
}