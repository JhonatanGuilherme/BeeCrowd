using System; 

class URI {

    static void Main(string[] args) { 

        while (true) {
      int N = Convert.ToInt32(Console.ReadLine());
      if (N == 0)
        break;
      int [,] M = new int [N, N];
      for (int i = 0; i < N; i++) {
          int count = i + 1;
          for(int j = 0; j < N; j++) {
              M[i, j] = Math.Abs(count);
              if (count == 1)
                  count -= 3;
              else
                  count -= 1;
          }
      }

      for (int i = 0; i < N; i++) {
          for (int j = 0; j < N; j++) {
            if (j == 0 && M[i, j] < 10)
              Console.Write("  " + M[i, j]);
            else if (j == 0 && M[i, j] < 100)
              Console.Write(" " + M[i, j]);
            else if (j == 0)
              Console.Write(M[i, j]);

            else if (M[i, j] < 10)
              Console.Write("   " + M[i, j]);
            else if (M[i, j] < 100)
              Console.Write("  " + M[i, j]);
            else
              Console.Write(" " + M[i, j]);
          }
          Console.Write("\n");
      }
      Console.Write("\n");
    }

    }

}