using System; 

class URI {

    static void Main(string[] args) { 

        int A = Convert.ToInt32(Console.ReadLine());
		for(int i = 0; i < 10; i++) {
			Console.WriteLine("N[{0}] = {1}", i, A);
			A *= 2;
    }

    }

}