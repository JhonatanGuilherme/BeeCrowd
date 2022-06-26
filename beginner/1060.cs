using System;

namespace CSharp{
    class Program{
        static void Main(string[] args){
            int A = 0;
            for (int i = 0; i < 6; i ++){
               double B = float.Parse(Console.ReadLine());
                if (B >= 0.0)
                    A ++;
            }
            Console.WriteLine("{0} valores positivos", A);
        }
    }
}
