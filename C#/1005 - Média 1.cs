using System; 

class URI {
    static void Main(string[] args) {
      double X = Convert.ToDouble(Console.ReadLine());
      double Y = Convert.ToDouble(Console.ReadLine());
      double R = ((X * 3.5) + (Y * 7.5)) / 11;
      Console.WriteLine("MEDIA = " + R.ToString("0.00000"));
    }
}