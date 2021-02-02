using System; 

class URI {

    static void Main(string[] args) { 

        long [] N = new long [61];
        N[0] = 0; N[1] = 1;
    
        int T = int.Parse(Console.ReadLine()), X = 0;
    
        for (int i = 2; i < 61; i++) {
          N[i] = N[i - 1] + N[i - 2];
        }
    
    		for (int i = 0; i < T; i++) {
          X = int.Parse(Console.ReadLine());
    			Console.WriteLine("Fib({0}) = {1}", X, N[X]);
        }

    }

}