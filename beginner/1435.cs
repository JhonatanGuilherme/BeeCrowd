using System; 

class URI {

    static void Main(string[] args) { 

        int N = 0;
    while (true) {
      N = int.Parse(Console.ReadLine());
      if (N == 0)
        break;
      int [,] M = new int [N, N];

      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          M[i, j] = 1;
        }
      }

      int X = 1;
      for (int i = 0; i < N / 2; i++) {
        for (int j = X; j < N - X; j++) {
          for (int k = X; k < N - X; k++) {
            if (j == X || k == X || j == N - X - 1 || k == N - X - 1)
              M[j, k] = X + 1;
          }
        }
        X ++;
      }

      for (int i = 0; i < N; i++) {
        Console.Write("  ");
          for (int j = 0; j < N; j++) {

            if (j == 0)
              Console.Write(M[i, j]);
            else if (M[i, j] >= 10)
              Console.Write("  " + M[i, j]);
            else
              Console.Write("   " + M[i, j]);
            if (j == N - 1)
              Console.Write("\n");

          }
      }
      Console.Write("\n");
    }
    }

}