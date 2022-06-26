using System; 

class URI {
  static void Main(string[] args) {
    int D = Convert.ToInt32(Console.ReadLine());
    int ANO = D / 365;
    D -= ANO * 365;
    int MES = D / 30;
    D -= MES * 30;
    Console.WriteLine(ANO + " ano(s)"); 
    Console.WriteLine(MES + " mes(es)");
    Console.WriteLine(D + " dia(s)");
  }
}
