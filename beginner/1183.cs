using System; 

class URI {

    static void Main(string[] args) { 

        double num = 0, soma = 0;
	  string nome = Console.ReadLine();
		for (int L = 0; L < 12; L++){
			for(int C = 0; C < 12; C++){
				num = double.Parse(Console.ReadLine());
				if(C > L)
					soma += num;
		  }			
 	  }

	  if (nome == "S")
			Console.WriteLine(soma);
		if (nome == "M")
			Console.WriteLine((soma / 66).ToString("0.0"));

    }

}