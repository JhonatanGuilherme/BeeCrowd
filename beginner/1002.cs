using System; 

class URI {
  static void Main(string[] args) {
    double Raio = Convert.ToDouble(Console.ReadLine());
    double R = 3.14159 * Math.Pow(Raio, 2);
    Console.WriteLine("A=" + R.ToString("0.0000"));
  }
}