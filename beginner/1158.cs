using System; 

class URI {

    static void Main(string[] args) { 

        int C = 0, C2 = 0, N = int.Parse(Console.ReadLine()), X = 0;
    string [] V = new string [2];

    for (int i = 0; i < N; i++) {
      C = 0; 
      C2 = 0;
      V = Console.ReadLine().Split();
      X = int.Parse(V[0]);
      while (C2 != int.Parse(V[1])){
        if (X % 2 != 0){
          C += X;
          C2 ++;
        }
        X++;
      }
      Console.WriteLine(C);
    }

    }

}