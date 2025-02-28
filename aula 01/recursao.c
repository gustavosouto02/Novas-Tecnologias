#include <stdio.h>
#include <math.h>

int suc(int n){
    return ++n;
}

int pred(int n){
    return --n;
}
/*
int soma(int n1, int n2){
    while(n1 != 0){
        n1 = pred(n1);
        n2 = suc(n2);
    }
    return n2;
}*/

int rsoma(int n1, int n2){
    if (n1 == 0)
        return n2;
    else 
        return rsoma(pred(n1), suc(n2));
}

int main(){
    int n1, n2;

    printf("Digite a soma: ");
    scanf("%d + %d", &n1, &n2);

    printf("A soma e : %d", rsoma(n1, n2));
}

