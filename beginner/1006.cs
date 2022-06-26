using System; 

class URI {
  static void Main(string[] args) {
    double X = Convert.ToDouble(Console.ReadLine());
    double Y = Convert.ToDouble(Console.ReadLine());
    double Z = Convert.ToDouble(Console.ReadLine());
    double R = ((X * 2) + (Y * 3) + (Z * 5)) / 10;
    Console.WriteLine("MEDIA = " + R.ToString("0.0"));
  }
}