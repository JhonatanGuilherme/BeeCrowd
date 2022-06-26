using System; 

class URI {

    static void Main(string[] args) { 

        int N = 0;
    string S = "";

    while (true) {

      S = Console.ReadLine();
      if (string.IsNullOrEmpty(S))
        break;
      N = int.Parse(S);

      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {

          if (i + j == N - 1)
            Console.Write(2);
          else if (i == j)
            Console.Write(1);
          else
            Console.Write(3);

        }
        Console.WriteLine("");
      }

    }

    }

}