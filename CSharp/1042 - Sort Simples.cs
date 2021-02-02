using System;

class MainClass {
    public static void Main (string[] args) {
        string[] V = Console.ReadLine().Split(' ');
	    int A = int.Parse(V[0]);
		int B = int.Parse(V[1]);
		int C = int.Parse(V[2]);
		if (A <= B && B <= C && A <= C)
			Console.WriteLine(A + "\n" + B + "\n" + C + "\n");
        else if (A <= B && B >= C && A <= C)
			Console.WriteLine(A + "\n" + C + "\n" + B + "\n");
		else if (A >= B && B <= C && A <= C)
			Console.WriteLine(B + "\n" + A + "\n" + C + "\n");
		else if (A >= B && B <= C && A >= C)
			Console.WriteLine(B + "\n" + C + "\n" + A + "\n");
        else if (A <= B && B >= C && A >= C)
			Console.WriteLine(C + "\n" + A + "\n" + B + "\n");
        else if (A >= B && B >= C && A >= C)
			Console.WriteLine(C + "\n" + B + "\n" + A + "\n");
        Console.WriteLine(A + "\n" + B + "\n" + C);
    }
}