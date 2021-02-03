using System; 

class URI {

    static void Main(string[] args) { 

        while (true)
		{
			int N = Convert.ToInt32(Console.ReadLine());
            string X = "";
			if (N == 0)
				break;
			else {
				for(int x = 1; x <= N; x++) {
					if (x == N) 
						X += x.ToString();
					else
					    X += x.ToString() + " ";
				}
                Console.WriteLine(X);
			}
		}

    }

}