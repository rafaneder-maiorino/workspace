#ifndef COMPLEXOS_H_INCLUDED
#define COMPLEXOS_H_INCLUDED

//Definição da representação de dados

typedef struct{
int real;
int img;
} Complex;

//Definição das operações sobre Complex

Complex *create(int real, int img); //cria um número complexo

Complex *sum(Complex *c1, Complex *c2); // soma dois números complexos c1 e c2, gerando um terceiro

Complex *Substr(Complex *c1, Complex *c2); //subtrai um número complexo c2 de outro c1, gerando um terceiro

Complex *multiply(Complex *c1, Complex *c2); //multiplica dois números complexos c1 e c2, gerando um terceiro

Complex *pot(Complex *c1, Complex *c2); //potencializa um número complexo c1 por outro c2, gerando um terceiro


#endif // COMPLEXOS_H_INCLUDED
