using System;
					
public class Program{
  public static void Main(){
	  string[] M = Console.ReadLine().Split();
	  double N1 = double.Parse(M[0]);
	  double N2 = double.Parse(M[1]);
	  double N3 = double.Parse(M[2]);
    double N4 = double.Parse(M[3]);
	  double MD = Math.Round(((N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10), 1);
	  Console.WriteLine("Media: " + MD.ToString("0.0"));
    if (MD > 6.9)
	    Console.WriteLine("Aluno aprovado.");
    else if (MD < 4.9)
	    Console.WriteLine("Aluno reprovado.");
    else{
      Console.WriteLine("Aluno em exame.");
      double NE = double.Parse(Console.ReadLine());      
      Console.WriteLine("Nota do exame: " + NE.ToString("0.0"));
  		double MDF = Math.Round((MD + NE) / 2, 1);
  		if (MDF > 4.9)
    		Console.WriteLine("Aluno aprovado." );
      else
        Console.WriteLine("Aluno reprovado.");
      Console.WriteLine("Media final: " + MDF.ToString("0.0"));}
	}
}