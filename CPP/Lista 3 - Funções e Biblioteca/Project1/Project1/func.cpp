#include <math.h>

// Questão 01
int dobro(int num)
{
	return 2 * num;
}

// Questão 02
int soma(int num_pri, int num_seg)
{
	return num_pri + num_seg;
}

int sub(int num_pri, int num_seg)
{
	return num_pri - num_seg;
}

int mult(int num_pri, int num_seg)
{
	return num_pri * num_seg;
}

int divi(int num_pri, int num_seg)
{
	return num_pri / num_seg;
}

// Questão 03
int nota(int nota_pri, int nota_seg)
{
	
	int media = (nota_pri + nota_seg) / 2;

	if (media < 5) {
		return 0;
	}
	else {
		return 1;
	}

}

// Questão 04
int equacao(int a, int b, int c)
{
	double delta = ((b*b) - 4 * a*c);

	double raiz = sqrt(delta);

	double x1 = ((-b + raiz) / (2 * a));
	double x2 = ((-b - raiz) / (2 * a));

	if (delta == 0)
	{
		return 1;
	}
	else if (delta > 0)
	{
		return 2;
	}
	else
	{
		return 0;
	}

}

// Questão 05
int triangulo(int x, int y, int z)
{

	if (x < y + z && y < x + z && z < x + y) {

		if (x == y && y == z) {
			return 3;
		}
		else if (x == y || x == z || y == z) {
			return 1;
		}
		else {
			return 2;
		}

	}

	else {
		return 0;
	}


}

// Questão 06
int mediaifce(int n1, int n2, int n3, int n4, int n5, int n6)
{
	int media1 = ((n1 + n2 + n3) / 3) * 2;
	int media2 = ((n4 + n5 + n6) / 3) * 3;

	int mediatotal = (media1 + media2) / 5;

	if (mediatotal >= 7)
	{
		return 1;
	}
	else
	{
		return 0;
	}

}

// Questão 07
int mediafinalifce(int nt1, int nt2, int nt3, int nt4, int nt5, int nt6)
{
	int mediafinal1 = ((nt1 + nt2 + nt3) / 3) * 2;
	int mediafinal2 = ((nt4 + nt5 + nt6) / 3) * 3;

	int mediafinaltotal = (mediafinal1 + mediafinal2) / 5;

	if (mediafinaltotal >= 7)
	{
		return 1;
	}
	else
	{
		return 0;
	}

}

int mediafinal(int nt1, int nt2, int nt3, int nt4, int nt5, int nt6)
{
	int mf1 = ((nt1 + nt2 + nt3) / 3) * 2;
	int mf2 = ((nt4 + nt5 + nt6) / 3) * 3;

	int mftotal = (mf1 + mf2) / 5;

	if (mftotal < 7)
	{
		int mfnecessaria = (10 - mftotal);
		return mfnecessaria;
	}

}

// Questão 08
int maiormenor(int lista[])
{
	int i, j, aux;

	for (i = 0; i < 4; i++)
	{
		for (j = (i + 1); j < 4; j++)
		{
			if (lista[j] < lista[i])
			{
				aux = lista[i];
				lista[i] = lista[j];
				lista[j] = aux;
			}
		}
	}
	int menorvar = lista[0];
	int maiorvar = lista[3];

	return (maiorvar - menorvar);

}

// Questão 09
double fatorial(double numf)
{
	double i = 1;
	double fatorial = 1;

	while (i <= numf)
	{
		fatorial = fatorial * i;
		i++;
	}
	
	return fatorial;
}

// Questão 10


// Questão 11
double serie(double nserie)
{
	double serieres = 0;
	int j = 0;

	for (int i = 25; i >= 1; i--)
	{
		j++;
			if ((i % 2) == 1)
			{
				serieres = serieres + (pow(nserie, i) / j);
			}
			else
			{
				serieres = serieres - (pow(nserie, i) / j);
			}
	}

	return serieres;

}

// Questão 12
double seriedes()
{
	double respserie = 0;
	double j = 0;

	for (double i = 100; i >= 1; i--)
	{
	
		respserie = respserie + (i / fatorial(j));
		j++;

	}

	return respserie;
}

// Questão 13
double serie13(double entradauser)
{
	double resserie13 = entradauser;
	int posneg = 0;

	for (int i = 3; i <= 13; i += 2)
	{
		if (posneg == 0)
		{
			resserie13 -= pow(entradauser, i) / fatorial(i);
			posneg = 1;
		}
		else
		{
			resserie13 += pow(entradauser, i) / fatorial(i);
			posneg = 0;
		}

	}
	return resserie13;
}

// Questão 14
double serie14(double userentrada)
{
	double resserie14 = 0;
	int i = 0;

	for ( i = 0; i <= 20; i++)
	{
		resserie14 += pow(userentrada, i) / fatorial(i);
	}

	return resserie14;
}

// Questão 15
double serie15(double valusuario)
{
	double resserie15 = 0;
	int posneg = 0;

	for (int i = 0; i <= 20; i += 2)
	{
		if (posneg == 0)
		{
			resserie15 -= pow(valusuario, i) / fatorial(i);
			posneg = 1;
		}
		else
		{
			resserie15 += pow(valusuario, i) / fatorial(i);
			posneg = 0;
		}
	}
	return resserie15;
}

// Questão 16
// A funcao 'fatorial()' ja foi utilizada nas questoes anteriores!