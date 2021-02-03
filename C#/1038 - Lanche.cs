using System;

class URI {
    public static void Main (string[] args) {
        string[] pedido = Console.ReadLine().Split();
    	int codigo = int.Parse(pedido[0]);
    	int quantidade = int.Parse(pedido[1]);
    	switch (codigo){
    	    case (1):
                Console.WriteLine("Total: R$ " + (4.00 * quantidade).ToString("0.00"));
    		    break;
    		case (2):
    			Console.WriteLine("Total: R$ " + (4.50 * quantidade).ToString("0.00"));
    			break;	
    		case (3):
    			Console.WriteLine("Total: R$ " + (5.00 * quantidade).ToString("0.00"));
    			break;			
    		case (4):
    			Console.WriteLine("Total: R$ " + (2.00 * quantidade).ToString("0.00"));
    			break;	
    		case (5):
    			Console.WriteLine("Total: R$ " + (1.50 * quantidade).ToString("0.00"));
    			break;
    		default:
    			break;
    	}
    }
}