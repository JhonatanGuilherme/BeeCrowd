using System; 

class URI {

    static void Main(string[] args) { 

        string [] V = Console.ReadLine().Split();
		int A = int.Parse(V[0]), N = 0;
		for (int i = 1; i < V.Length; i ++) {
			if (int.Parse(V[i]) > 0 && N == 0)
				N = int.Parse(V[i]);
		}
		int S = A;
		for (int j = 1; j < N; j ++) {
			S += A + j;
		}
		Console.WriteLine(S);

    }

}