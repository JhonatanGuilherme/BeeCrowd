using System;

class URI {

  static void ImprimirArray (int [] A, int contador, string tipo) {
    for (int i = 0; i < contador; i++) {
      Console.WriteLine("{0}[{1}] = {2}", tipo, i, A[i]);
    }
  }
  
  public static void Main (string[] args) {

    int contPar = 0, contImpar = 0, X = 0;
    int [] impar = new int [15], par = new int [15];

    for (int i = 0; i < 15; i++) {
      X = int.Parse(Console.ReadLine());
      if (X % 2 == 0) {
        par[contPar] = X;
        contPar ++;
      }
      else {
        impar[contImpar] = X;
        contImpar ++;
      }
      if (contPar == 5) {
        ImprimirArray(par, contPar, "par");
        contPar = 0;
      }
        
      if (contImpar == 5){
        ImprimirArray(impar, contImpar, "impar");
        contImpar = 0;
      }
        
    }

    if (contImpar > 0) {
      ImprimirArray(impar, contImpar, "impar");
    }
    if (contPar > 0)
      ImprimirArray(par, contPar, "par");
    
    


  }
}