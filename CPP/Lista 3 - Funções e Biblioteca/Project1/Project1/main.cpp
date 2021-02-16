// IFCE CAMPUS FORTALEZA - 2019.1
// ENGENHARIA DE MECATRÔNICA - PROGRAMAÇÃO AVANÇADA
// Prof. Dr. Pedro Pedrosa Rebouças Filho | https://professorpedrosa.com
// Resolução de Iágson Carlos Lima Silva - Matrícula: 20181015010068 | iagsoncarlos@gmail.com

//----------------------------------------------------------------------------------------------------------------------------

#include <iostream>
#include "func.h"

using namespace std;

int main()
{

	// Declaração do Menu principal

	int op;

	do
	{

		cout << "Digite um valor para funcao, conforme menu abaixo:\n\n------------------------- MENU -------------------------\n" << endl;
		cout << " 01 - Questao 01: Ler um numero, calcular o dobro..." << endl;
		cout << " 02 - Questao 02: Faca as funcoes de matematica..." << endl;
		cout << " 03 - Questao 03: Ler duas notas, passar estas..." << endl;
		cout << " 04 - Questao 04: Dados tres valores A, B e C de..." << endl;
		cout << " 05 - Questao 05: Fazer uma funcao para ler tres..." << endl;
		cout << " 06 - Questao 06: Fazer uma funcao para ler..." << endl;
		cout << " 07 - Questao 07: Faca uma funcao que calcule..." << endl;
		cout << " 08 - Questao 08: Passe quatro numeros como..." << endl;
		cout << " 09 - Questao 09: Fazer uma funcao que..." << endl;
		cout << " 10 - Questao 10: Faca uma funcao que receba..." << endl;
		cout << " 11 - Questao 11: B = {[(X^25)/1]-[(X^24)/2]+..." << endl;
		cout << " 12 - Questao 12: S = {[(100/0!)+(99/1!)+(98+..." << endl;
		cout << " 13 - Questao 13: C = X - {[(x ^ 3) / 3!] +..." << endl;
		cout << " 14 - Questao 14: e^x = (x^0) + {[(x^1)/1!]..." << endl;
		cout << " 15 - Questao 15: COSSENO = 1 - {[(x^2)/2!]..." << endl;
		cout << " 16 - Questao 16: Resolva as questoes de 12 a..." << endl;

		cout << "\n--------------------------------------------------------\n 00 - SAIR DO PROGRAMA" << endl;
		cout << " 99 - INFORMACAOES DO DESENVOLVEDOR" << endl;
		cout << "--------------------------------------------------------" << endl;

		cout << "\nDigite aqui: ";

		cin >> op;
		system("CLS");

		// Chamada das funcões de cada opção do menu principal

		switch (op)
		{
		case 0:
			system("exit");
			system("CLS");
			break;

		case 1:
			// Questão 01
			int num;

			cout << "Questao 01: Ler um numero, calcular o dobro e retornar seu valor.\n" << endl;

			cout << "Digite um valor: ";
			cin >> num;

			cout << "\nResposta: " << dobro(num) << endl << endl;
			system("pause");
			system("CLS");

			break;
			

		case 2:
			// Questão 02
			int num_pri, num_seg, opera;

			cout << "Questao 02: Faca as funcoes de matematica basica entre dois numeros: subtracao, divisao, multiplicacao e soma. Os dois numeros devem ser entrada da funcao e o resultado deve ser o retorno.\n" << endl;

			cout << "Digite o primeiro numero: ";
			cin >> num_pri;
			cout << "Digite o segundo numero: ";
			cin >> num_seg;

			cout << "\n\nDigite a operacao conforme submenu abaixo: \n" << endl;

			cout << "---------------- SUBMENU ----------------" << endl;
			cout << "01 - SOMA" << endl;
			cout << "02 - SUBTRACAO" << endl;
			cout << "03 - MULTIPLICACAO" << endl;
			cout << "04 - DIVISAO" << endl;
			cout << "\n00 - Sair\n\nDigite aqui : ";
			cin >> opera;

			switch (opera)
			{
			case 0:
				system("exit");
				system("CLS");
				break;

			case 1:
				cout << "\nResposta: " << soma(num_pri, num_seg) << endl << endl;
				system("pause");
				system("CLS");
				break;

			case 2:
				cout << "\nResposta: " << sub(num_pri, num_seg) << endl << endl;
				system("pause");
				system("CLS");
				break;

			case 3:
				cout << "\nResposta: " << mult(num_pri, num_seg) << endl << endl;
				system("pause");
				system("CLS");
				break;

			case 4:
				cout << "\nResposta: " << divi(num_pri, num_seg) << endl << endl;
				system("pause");
				system("CLS");
				break;

			default:
				cout << "\nOPERACAO INVALIDA!\n" << endl;
				system("pause");
				system("CLS");
				break;
			}
			break;
			system("pause");

		case 3:
			// Questão 03
			int nota_pri, nota_seg;

			cout << "Questao 03: Ler duas notas, passar estas como entrada de uma funcao que calcule a media e retornar 1 se for aprovado e zero se for reprovado, a media para aprovacao e de no minimo 5,0.\n" << endl;

			cout << "Digite a primeira nota: ";
			cin >> nota_pri;
			cout << "Digite a segunda nota: ";
			cin >> nota_seg;

			if (nota(nota_pri, nota_seg) == 0) {
				cout << "\nResposta: REPROVADO!\n" << endl;
				system("pause");
				system("CLS");
			}
			else {
				cout << "\nResposta: APROVADO!\n" << endl;
				system("pause");
				system("CLS");
			}
			break;
			system("pause");

		case 4:
			// Questão 04
			int a, b, c;

			cout << "Questao 04: Dados tres valores A, B e C de uma equacao do segundo grau (Ax2+Bx+C=0), faca uma funcao para calcular o valor das raizes, se para os valores fornecidos for possivel determinar raizes reais. O retorno da funcao deve ser a quantidade de raizes, e as possiveis raizes devem ser colocadas como variavel de entrada da funcao.\n" << endl;

			cout << "Dada a equacao: ax^2 + bx + c = 0, digite os valores de a, b e c:\n" << endl;

			cout << "Digite o valor para 'a': ";
			cin >> a;
			cout << "Digite o valor para 'b': ";
			cin >> b;
			cout << "Digite o valor para 'c': ";
			cin >> c;

			if (equacao( a, b, c) == 1)
			{
				cout << "\nResposta: Valor de 'delta' igual a 0, logo as raizes sao iguais!\n" << endl;
			}
			else if (equacao(a, b, c) == 2)
			{
				cout << "\nResposta: Valor de 'delta' e maior que 0, logo exitem duas raizes reais!\n" << endl;
			}
			else
			{
				cout << "\nResposta: Valor de 'delta' e menor que 0, logo nao exitem raizes reais!\n" << endl;

			}

			system("pause");
			system("CLS");
			break;

		case 5:
			// Questão 05

			int x, y, z;

			cout << "Questao 05: Fazer uma funcao para ler tres numeros, estes numeros podem ser o comprimento dos lados de um triangulo. Dizer se estes numeros podem ser de um triangulo, caso positivo, classificar em equilatero, isoscele ou escaleno. Caso nao seja triangulo a funcao deve retornar 0, se for isosceles deve retornar 1, se for escaleno deve retorna 2 e se for equilatero retornar 3.\n" << endl;

			cout << "Digite os valores para os lados de um triangulo:\n" << endl;
			cout << "Lado 'x': ";
			cin >> x;
			cout << "Lado 'y': ";
			cin >> y;
			cout << "Lado 'z': ";
			cin >> z;

			if (triangulo(x, y, z) == 3)
			{
				cout << "\nResposta: Triangulo equilatero: possui os tres lados com medidas iguais 'x' " << x << ".\n" << endl;
			}
			else if (triangulo(x, y, z) == 1)
			{
				cout << "\nResposta: Triangulo isosceles: possui dois lados com medidas iguais, sendo: 'x' = " << x << ", 'y' = " << y << " e 'z' = " << z << ".\n" << endl;
			}
			else if (triangulo(x, y, z) == 2)
			{
				cout << "\nResposta: Triangulo escaleno: possui os tres lados com medidas diferentes, sendo: 'x' = " << x << ", 'y' = " << y << " e 'z' = " << z << ".\n" << endl;
			}
			else {
				cout << "\nResposta: Nao e um triangulo!\n" << endl;
			}

			system("pause");
			system("CLS");
			break;


		case 6:
			// Questão 06

			int n1, n2, n3, n4, n5, n6;

			cout << "Questao 06: Fazer uma funcao para ler tres notas (sistema do IFCE), Calcular a media (ponderada), dizer se foi aprovado por media (7,0). Deve - se retornar desta funcao valor 1 se for aprovado e 0 se for reprovado.\n" << endl;


			cout << "PRIMEIRA ETAPA:\n" << endl;
			cout << "Digite o valor da primeira nota: ";
			cin >> n1;
			cout << "Digite o valor da segunda nota: ";
			cin >> n2;
			cout << "Digite o valor da terceira nota: ";
			cin >> n3;

			cout << "\nSEGUNDA ETAPA:\n" << endl;
			cout << "Digite o valor da primeira nota: ";
			cin >> n4;
			cout << "Digite o valor da segunda nota: ";
			cin >> n5;
			cout << "Digite o valor da terceira nota: ";
			cin >> n6;

			if (mediaifce(n1, n2, n3, n4, n5, n6) == 1)
			{
				cout << "\nResposta: Aprovado!\n" << endl;
			}
			else {
				cout << "\nResposta: Reprovado!\n" << endl;
			}

			system("pause");
			system("CLS");
			break;

		case 7:
			// Questão 07

			cout << "Questao 07: Faca uma funcao que calcule quanto o aluno precisaria tirar na final quando a funcao da questao 6 retornar 0.\n" << endl;

			int nt1, nt2, nt3, nt4, nt5, nt6;
			int mfnecessaria;

			cout << "PRIMEIRA ETAPA:\n" << endl;
			cout << "Digite o valor da primeira nota: ";
			cin >> nt1;
			cout << "Digite o valor da segunda nota: ";
			cin >> nt2;
			cout << "Digite o valor da terceira nota: ";
			cin >> nt3;

			cout << "\nSEGUNDA ETAPA:\n" << endl;
			cout << "Digite o valor da primeira nota: ";
			cin >> nt4;
			cout << "Digite o valor da segunda nota: ";
			cin >> nt5;
			cout << "Digite o valor da terceira nota: ";
			cin >> nt6;

			if (mediafinalifce(nt1, nt2, nt3, nt4, nt5, nt6) >= 7)
			{
				cout << "\nResposta: Aprovado!\n" << endl;
			}
			else
			{
				cout << "\nResposta: Reprovado!\n" << endl;

				mfnecessaria = mediafinal( nt1, nt2, nt3, nt4, nt5, nt6);
				cout << "Nota necessaria para aprovacao na prova final igual a " << mfnecessaria << ".\n" << endl;

			}
			system("pause");
			system("CLS");
			break;

		case 8:
			// Questão 08

			cout << "Questao 08: Passe quatro numeros como parametro de entrada de uma funcao, retorne a diferenca entre o maior e o menor valor lido.\n" << endl;

			int lista[4];

			cout << "Digite o primeiro valor: ";
			cin >> lista[0];
			cout << "Digite o segundo valor: ";
			cin >> lista[1];
			cout << "Digite o terceiro valor: ";
			cin >> lista[2];
			cout << "Digite o quarto valor: ";
			cin >> lista[3];

			cout << "\nDiferenca entre o maior e o menor valor e igual a: " << maiormenor(lista) << ".\n" << endl;

			system("pause");
			system("CLS");
			break;

		case 9:
			// Questão 09
			double numf;

			cout << "Fazer uma funcao que calcule o valor de N! (Fatorial de N), sendo que o valor inteiro de N é passado como entrada da funcao. O programa devera retornar um valor que identifique que aconteceu um erro quando entrar um valor negativo e tratar adequadamente para 0! e 1!.\n" << endl;

			cout << "Digite um numero aqui: ";
			cin >> numf;

			if (numf < 0)
			{
				cout << "\nO numero digitado nao e positivo!" << endl << endl;
			}
			else if (numf == 1 || numf == 0)
			{
				cout << "\nO Fatorial do numero digitado e 1." << endl << endl;
			}
			else
			{
				cout << "\nO Fatorial do numero digitado e igual a: " << fatorial(numf) << ".\n" << endl;

			}

			system("pause");
			system("CLS");
			break;

		case 10:
			// Questão 10

			cout << "Faca uma funcao que receba quatro valores de entrada referentes a duas cidades. No primeiro parametro deve-se colocar a populacao da cidade A, no segundo parametro deve-se colocar a taxa de crescimento da cidade A, no terceiro parametro deve-se colocar a populacao da cidade B e, por ultimo, na quarta posicao deve-se colocar a taxa de crescimento da cidade B. Esta funcao deve retornar quantos anos serao necessarios para a cidade A ter uma populacao maior que a cidade B.\n" << endl;





			system("pause");
			system("CLS");
			break;

			//

		case 11:
			// Questão 11

			cout << "B = {[(X^25)/1]-[(X^24)/2]+[(X^23)/3]-[(X^22)/4]+...+[X/25]\n" << endl;

			long nserie;

			cout << "Digite um valor para o 'X': ";
			cin >> nserie;

			cout << "\nResposta: " << serie(nserie) << ".\n" << endl;

			system("pause");
			system("CLS");
			break;


		case 12:
			// Questão 12

			cout << "S = {[(100/0!)+(99/1!)+(98/2!)+(97/3!)+...+(1/99!)]}.\n" << endl;

			cout << "\nResposta: " << seriedes() << ".\n" << endl;

			system("pause");
			system("CLS");
			break;


		case 13:
			// Questão 13

			cout << "Questao 13: C = X - {[(x^3)/3!]+[(x^5)/5!]-[(x^7)/7!]+...+[(x^13)/13!].\n" << endl;

			double entradauser;

			cout << "Digite um valor para o 'X': ";
			cin >> entradauser;

			entradauser = serie13(entradauser);

			cout << "\nResposta: " << entradauser << ".\n" << endl;

			system("pause");
			system("CLS");
			break;

		case 14:
			// Questão 14

			cout << "Questao 14: e^x = (x^0) + {[(x^1)/1!]+[(x^2)/2!]+[(x^3)/3!]+...+[(x^20)/20!]}.\n" << endl;
			
			double valoruser;

			cout << "Digite um valor para o 'X': ";
			cin >> valoruser;

			valoruser = serie14(valoruser);

			cout << "\nResposta: " << valoruser << ".\n" << endl;

			system("pause");
			system("CLS");
			break;

		case 15:
			// Questão 15

			cout << "Questao 15: COSSENO = 1 - {[(x^2)/2!]+[(x^4)/4!]-[(x^6)/6!]+...+[(x^20)/20!].\n" << endl;

			double valusuario;

			cout << "Digite um valor para o 'X': ";
			cin >> valusuario;

			valusuario = serie15(valusuario);

			cout << "\nResposta: " << valusuario << ".\n" << endl;

			system("pause");
			system("CLS");
			break;

		case 16:
			// Questão 16

			cout << "Questao 16: Resolva as questoes de 12 a 15, utilizando dentro do calculo a funcao de fatorial feita questao 9.\n" << endl;

			cout << "A funcao 'fatorial()' ja foi utilizada nas questoes anteriores!\n" << endl;

			system("pause");
			system("CLS");
			break;


		case 99:
			// Informações do desenvolvedor

			cout << "-------------------------------- INFORMACOES DO DESENVOLVEDOR --------------------------------\n\nIFCE CAMPUS FORTALEZA - 2019.1\nENGENHARIA DE MECATRONICA - PROGRAMACAO AVANCADA\nProf. Dr. Pedro Pedrosa Reboucas Filho | https://professorpedrosa.com\nResolucao de Iagson Carlos Lima Silva - Matricula: 20181015010068 | iagsoncarlos@gmail.com\n\n----------------------------------------------------------------------------------------------\n" << endl;

			system("pause");
			system("CLS");
			break;

		default:
			cout << "\nOPERACAO INVALIDA!\n" << endl;
			system("pause");
			system("CLS");
			break;
		}
	} while (op != 00);

	system("pause");
}