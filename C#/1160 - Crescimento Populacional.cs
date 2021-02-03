using System; 

class URI {

    static void Main(string[] args) { 

    int CONTADOR = 0, PA = 0, PB = 0, T = int.Parse(Console.ReadLine());
    double G1 = 0, G2 = 0;
    string [] S;

    for (int i = 0; i < T; i++) {
      
      S = Console.ReadLine().Split();
      PA = int.Parse(S[0]); 
      PB = int.Parse(S[1]); 
      G1 = double.Parse(S[2]); 
      G2 = double.Parse(S[3]);

      while (PA <= PB && CONTADOR <= 100) {

        PA += (int)((PA * G1) / 100);
        PB += (int)((PB * G2) / 100);
        CONTADOR ++;

      }

      if (CONTADOR > 100)
        Console.WriteLine("Mais de 1 seculo.");
      else 
        Console.WriteLine("{0} anos.", CONTADOR);

      CONTADOR = 0;
    }

    }

}