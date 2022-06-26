using System; 

class URI {

    static void Main(string[] args) { 

        decimal X = Convert.ToDecimal(Console.ReadLine());
		for(int i = 0; i < 100; i++) {
			Console.WriteLine($"N[{i}] = {Math.Round(X, 4).ToString("0.0000")}");
			X /= 2;
		}

    }

}