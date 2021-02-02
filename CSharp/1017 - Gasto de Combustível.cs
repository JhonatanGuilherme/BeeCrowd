using System; 

class URI {
    static void Main(string[] args) {
        double TP = Convert.ToDouble(Console.ReadLine());
	    double VM = Convert.ToDouble(Console.ReadLine());
		double R = (TP * VM) / 12;
		Console.WriteLine(R.ToString("0.000"));
    }
}