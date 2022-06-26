using System; 

class URI {

    static void Main(string[] args) { 

        bool primo = true;
    int N = int.Parse(Console.ReadLine()), X = 0;

		for(int i = 0; i < N; i++) {

			X = int.Parse(Console.ReadLine());
			primo = true;

      for (int j = 2; j < X; j++) {

        if (X % j == 0)
          primo = false;

      }

      if (primo == true) 
        Console.WriteLine("{0} eh primo", X);
      else 
        Console.WriteLine("{0} nao eh primo", X);
	
    }

    }

}