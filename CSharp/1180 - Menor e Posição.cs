using System; 

class URI {

    static void Main(string[] args) { 

        int menor = 1000, posicao = 0;
    int N = int.Parse(Console.ReadLine());
		string [] array = Console.ReadLine().Split();

    for (int i = 0; i < N; i++) {

			if (menor > int.Parse(array[i])) {
       	menor = int.Parse(array[i]);
    	  posicao = i;
      }		 

		}
    Console.WriteLine("Menor valor: {0}" , menor);
		Console.WriteLine("Posicao: {0}", posicao);

    }

}