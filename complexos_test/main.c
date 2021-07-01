#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "Complexos.h"

int main()
{
    int r1,r2,i1,i2;

    printf("\nDigite o primeiro numero real (r1): ");
    scanf("%d",&r1);
    printf("\nDigite o primeiro numero imaginario (i1): ");
    scanf("%d",&i1);

    printf("\nDigite o segundo numero real (r2): ");
    scanf("%d",&r2);
    printf("\nDigite o segundo numero imaginario (i2): ");
    scanf("%d",&i2);

    // Criando os no's complexos:
    Complex *c1 = (Complex*)malloc(sizeof(Complex));
    Complex *c2 = (Complex*)malloc(sizeof(Complex));
    c1 = create(r1,i1);
    c2 = create(r2,i2);

    // Somando os no's complexos:
    Complex *soma = (Complex*)malloc(sizeof(Complex));
    soma = sum(c1, c2);

    // Subtraindo os no's complexos:
    Complex *subtrai = (Complex*)malloc(sizeof(Complex));
    subtrai = Substr(c1, c2);

    // Multiplicando os no's complexos:
    Complex *mult = (Complex*)malloc(sizeof(Complex));
    mult = multiply(c1,c2);

    // Potenciação dos no's complexos:
    Complex *poten = (Complex*)malloc(sizeof(Complex));
    poten = pot(c1,c2);

    // Imprimindo dados na tela:
    printf("\n\n Resultado da Soma: %d + %di", soma->real, soma->img);
    printf("\n\n Resultado da Subtracao: %d + %di", subtrai->real, subtrai->img);
    printf("\n\n Resultado da Multiplicacao: %d + %di", mult->real, mult->img);
    printf("\n\n Resultado da Potenciacao: %d + %di\n", poten->real, poten->img);

    // Liberando espaço de memória alocado no HEAP:
    free(c1);
    free(c2);
    free(soma);
    free(subtrai);
    free(mult);
    free(poten);

    return 0;
}
