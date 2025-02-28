#include <stdio.h>
#include <math.h>

int main(){

int n, soma = 0;

printf("Digite um numero n: ");
scanf("%d", &n);

for (int i = 1, j=1; j<=n;j++, i+=2){
	soma= soma + i;
};
printf("O quadrado do numero %d e : %d", n, soma) ;

}