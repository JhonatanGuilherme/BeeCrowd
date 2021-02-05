#include <stdio.h>
 
int main() {
 
  char S1[50], S2[50], S3[50];
  scanf("%s", S1);
  setbuf(stdin, NULL);
  scanf("%s", S2);
  setbuf(stdin, NULL);
  scanf("%s", S3);
  setbuf(stdin, NULL);

  if (strcmp(S1, "vertebrado") == 0) {
    if (strcmp(S2, "ave") == 0) {
      if (strcmp(S3, "carnivoro") == 0)
        printf("aguia\n");
      if (strcmp(S3, "onivoro") == 0)
        printf("pomba\n");
    }
    if (strcmp(S2, "mamifero") == 0) {
      if (strcmp(S3, "onivoro") == 0)
        printf("homem\n");
      if (strcmp(S3, "herbivoro") == 0)
        printf("vaca\n");
    }
  }
    
  if (strcmp(S1, "invertebrado") == 0) {
    if (strcmp(S2, "inseto") == 0) {
      if (strcmp(S3, "hematofago") == 0)
        printf("pulga\n");
      if (strcmp(S3, "herbivoro") == 0)
        printf("lagarta\n");
    }
      
    if (strcmp(S2, "anelideo") == 0) {
      if (strcmp(S3, "hematofago") == 0)
        printf("sanguessuga\n");
      if (strcmp(S3, "onivoro") == 0)
        printf("minhoca\n");
    }  
  }
 
    return 0;
}