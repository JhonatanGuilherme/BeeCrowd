using System; 

class URI {

    static void Main(string[] args) { 

        bool perfeito = false;
            int N = int.Parse(Console.ReadLine()), X = 0, soma = 0;

            for (int i = 0; i < N; i++)
            {
                X = int.Parse(Console.ReadLine());
                for (int j = 1; j < X; j++)
                {

                    soma += j;
                    if (soma == X)
                        perfeito = true;
                }
                Console.WriteLine(perfeito ? X + " eh perfeito" : X + " nao eh perfeito");
                soma = 0;
                perfeito = false;
            }

    }

}