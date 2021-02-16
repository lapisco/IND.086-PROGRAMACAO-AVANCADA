// IFCE CAMPUS FORTALEZA - 2019.1
// ENGENHARIA DE MECATRÔNICA - PROGRAMAÇÃO AVANÇADA
// Prof. Dr. Pedro Pedrosa Rebouças Filho | https://professorpedrosa.com
// Resolução de Iágson Carlos Lima Silva - Matrícula: 20181015010068 | iagsoncarlos@gmail.com

//----------------------------------------------------------------------------------------------------------------------------


#include <iostream>
#include "func.h";

using namespace std;

int main()
{
	int op;

	// Interações com o usuário através do Menu Principal
	do
	{
	cout << "	-- Digite a opcao desejada do Menu abaixo! --\n\n" << endl;
	cout << "----------------- MENU PRINCIPAL -----------------\n\n 01 - Vetor\n 02 - Matriz" << endl;
	cout << "\n 00 - SAIR\n--------------------------------------------------" << endl;
	cout << "\nDigite aqui: ";
	cin >> op;

		switch (op)
		{
		case 0:
			system("exit");
			system("CLS");
			break;

		case 1:
			system("CLS");
			cout << "	-- Digite a opcao desejada do Menu abaixo! --\n\n" << endl;
			cout << "MENU PRINCIPAL > VETOR\n\n" << endl;

			// Questões de Vetores

			int op1;

			do
			{
				cout << "------------------------ SUBMENU ------------------------\n" << endl;
				cout << " 01 - Questao 1 - Preencher um vetor com 10 numeros..." << endl;
				cout << " 02 - Questao 2 - Preencher um vetor com 10 numeros..." << endl;
				cout << " 03 - Questao 3 - Preencher um vetor com 10 numeros..." << endl;
				cout << " 04 - Questao 4 - Preencher um vetor com 10 numeros..." << endl;
				cout << " 05 - Questao 5 - Preencher um vetor com numeros in..." << endl;
				cout << " 06 - Questao 6 - Faca um programa para ler 10 nume..." << endl;
				cout << "\n 00 - VOLTAR\n---------------------------------------------------------" << endl;
				cout << "\nDigite aqui: ";
				cin >> op1;

				// Submenu das questões de vetor

				switch (op1){

				case 0: {
					system("exit");
					system("CLS");
					break;
				}
				case 1:	{

					system("CLS");
					cout << "Questao 1 - Preencher um vetor com 10 numeros. Indique o maior numero ao varrer o vetor preenchido.\n" << endl; // Questionário
					// Código
					
					int vet[10];
					int valorMaior, valorMenor;
					valorMaior = valorMenor = 0;

					cout << "Digite o valor para cada posicao do vetor!\n" << endl;
					criarVetor(vet, valorMaior, valorMenor);

					cout << "\nMaior valor: " << valorMaior << endl << endl;

					system("PAUSE");
					system("CLS");
					break;
				}
				case 2: {

					system("CLS");
					cout << "Questao 2 - Preencher um vetor com 10 numeros. Indique o maior e o menor numero, e forneca a diferenca entre eles.\n" << endl; // Questionário
					// Código

					int vet[10];
					int valorMaior, valorMenor, valorDiferenca;
					valorDiferenca = valorMaior = valorMenor = 0;

					cout << "Digite o valor para cada posicao do vetor!\n" << endl;
					criarVetor(vet,valorMaior, valorMenor);

					valorDiferenca = (valorMaior - valorMenor);

					cout << "\nMaior valor: " << valorMaior << "\nMenor valor: " << valorMenor << "\n\nDiferenca: " << valorDiferenca << endl << endl;

					system("PAUSE");
					system("CLS");
					break;
				}
				case 3: {

					system("CLS");
					cout << "Questao 3 - Preencher um vetor com 10 números. Retorne quais são os números ímpares deste vetor.\n" << endl; // Questionário
					// Código

					int vet[10];
					int valor, valorMaior, valorMenor;
					valor = valorMaior = valorMenor = 0;

					cout << "Digite o valor para cada posicao do vetor!\n" << endl;
					criarVetor(vet, valorMaior, valorMenor);

					cout << "Valores do vetor que sao impares:\n" << endl;

					numeroImpar(vet, valor);

					cout << "\n\n";

					system("PAUSE");
					system("CLS");
					break;
				}
				case 4:
					system("CLS");
					cout << "Questao 4 - Preencher um vetor com 10 numeros. Retorne quais sao os numeros primos deste vetor.\n" << endl; // Questionário

					int vet[10];
					int valor, valorMaior, valorMenor;
					valor = valorMaior = valorMenor = 0;

					cout << "Digite o valor para cada posicao do vetor!\n" << endl;
					criarVetor(vet, valorMaior, valorMenor);

					consultaPrimo(vet);

					system("pause");
					system("CLS");
					break;

				case 5: {
					system("CLS");
					cout << "Questao 5 - Preencher um vetor com numeros inteiros (8unidades); solicitar um número do teclado. Pesquisar se esse numero existe no vetor. Se existir, imprimir em qual posicao do vetor. Se nao existir, imprimir MSG que nao existe.\n" << endl; // Questionário
					// Código

					int vet[10];
					int valorMaior, valorMenor, valorUsuario;
					valorUsuario = valorMaior = valorMenor = 0;

					cout << "Digite o valor para cada posicao do vetor!\n" << endl;
					criarVetor(vet, valorMaior, valorMenor);

					cout << "	-- Buscar valor no vetor --\n\nDigite o valor aqui: ";
					consultarVetor(vet, valorUsuario);

					cout << "\n\n";

					system("PAUSE");
					system("CLS");
					break;
				}
				case 6: {
					system("CLS");
					cout << "Questao 6 - Faca um programa para ler 10 numeros diferentes a serem armazenados em um vetor. Os numeros deverao ser armazenados no vetor na ordem em que forem lidos, sendo que, caso o usuario digite um numero que ja foi digitado anteriormente, o programa devera pedir a ele para digitar outro numero. Note que cada valor digitado pelo usuario deve ser pesquisado no vetor, verificando se ele existe entre os numeros que ja foram fornecidos. Exiba na tela o vetor final que foi digitado.\n" << endl; // Questionário
					// Código

					int vet[10];
					int valor = 0;

					cout << "Digite o valor para cada posicao do vetor!\n" << endl;
					criaConsulta(vet, valor);

					mostrarVetor(vet);

					cout << "\n\n";

					system("PAUSE");
					system("CLS");
					break;
				}
				default: {
					cout << "\nOpcao Invalida!\n" << endl;
					system("pause");
					system("CLS");
					break;
				}
				}	   				 

			} while (op1 != 00);

			system("pause");
			system("CLS");
			break;

		case 2:
			system("CLS");
			cout << "	-- Digite a opcao desejada do Menu abaixo! --\n\n" << endl;
			cout << "MENU PRINCIPAL > MATRIZ\n\n" << endl;

			// Questões de Matrizes

			int op2;

			do
			{
				cout << "------------------------ SUBMENU ------------------------\n" << endl;
				cout << " 07 - Questao 7 - Preencher uma matriz 3x3 e imprimir." << endl;
				cout << " 08 - Questao 8 - Criar um algoritmo que leia os el..." << endl;
				cout << " 09 - Questao 9 - Desenvolva um algoritmo que receb..." << endl;
				cout << " 10 - Questao 10 - Criar um algoritmo que leia os e..." << endl;
				cout << " 11 - Questao 11 - Criar um algoritmo que leia os e..." << endl;
				cout << " 12 - Questao 12 - Leia uma matriz de tamanho 10x3 ..." << endl;
				cout << " 13 - Questao 13 - Calcular e imprimir na tela uma ..." << endl;
				cout << " 14 - Questao 14 - Faca um programa que permita ao ..." << endl;
				cout << "\n 00 - VOLTAR\n---------------------------------------------------------" << endl;
				cout << "\nDigite aqui: ";
				cin >> op2;

				// Submenu das questões de matriz

				switch (op2)
				{
				case 0: {
					system("exit");
					system("CLS");
					break;
				}
				case 7: {
					system("CLS");
					cout << "Questao 7 - Preencher uma matriz 3x3 e imprimir.\n" << endl; // Questionário
					// Código

					int matriz[3][3];

					cout << "	-- Digite os valores para a Matriz [3][3] --\n" << endl;

					criarMatriz(matriz);

					cout << "	-- Matriz [3][3] --\n" << endl;

					imprimirMatriz(matriz);

					system("PAUSE");
					system("CLS");
					break;
				}
				case 8: {
					system("CLS");
					cout << "Questao 8 - Criar um algoritmo que leia os elementos de uma matriz inteira de 3x3 e imprimir outra matriz multiplicando cada elemento da primeira matriz por 2.\n" << endl; // Questionário
					// Código

					int matriz[3][3];
					int valor = 0;

					cout << "	-- Digite os valores para a Matriz [3][3] --\n" << endl;
					criarMatriz(matriz);

					cout << "\nDigite o valor multiplicador de cada elemento da Matriz [3][3]: ";
					cin >> valor;
					multiplicadorMatriz(matriz, valor);

					cout << "\n\n";

					cout << "	-- Matriz [3][3] --\n" << endl;
					imprimirMatriz(matriz);

					system("PAUSE");
					system("CLS");
					break;
				}
				case 9: {
					system("CLS");
					cout << "Questao 9 - Desenvolva um algoritmo que recebe 6 valores numericos inteiros numa matriz 2x3 e mostre a soma destes 6 numeros.\n" << endl; // Questionário
					// Código

					int matriz[2][3];

					cout << "	-- Digite os valores para a Matriz [2][3] --\n" << endl;
					criarMatriz2(matriz);

					cout << "	-- Matriz [2][3] --\n" << endl;
					imprimirMatriz2(matriz);

					cout << "\nA soma de todos os elementos da Matriz e [" << somadorMatriz2(matriz) << "].\n" << endl;

					system("PAUSE");
					system("CLS");
					break;
				}
				case 10: {
					system("CLS");
					cout << "Questao 10 - Criar um algoritmo que leia os elementos de uma matriz inteira de 4 x 4 e imprimir os elementos da diagonal principal.\n" << endl; // Questionário
					// Código

					int matriz[4][4];

					cout << "	-- Digite os valores para a Matriz [4][4] --\n" << endl;
					criarMatriz4(matriz);

					cout << "\n";

					cout << "	-- Matriz [4][4] --\n" << endl;
					imprimirDiagonal4(matriz);

					system("PAUSE");
					system("CLS");
					break;
				}
				case 11: {
					system("CLS");
					cout << "Questao 11 - Criar um algoritmo que leia os elementos de uma matriz inteira de 3 x 3 e imprimir todos os elementos, exceto os elementos da diagonal principal.\n" << endl; // Questionário
					// Código

					int matriz[3][3];

					cout << "	-- Digite os valores para a Matriz [3][3] --\n" << endl;
					criarMatriz(matriz);

					cout << "\n";

					cout << "	-- Matriz [3][3] --\n" << endl;
					ocultarDiagonal(matriz);

					system("PAUSE");
					system("CLS");
					break;
				}
				case 12: {
					system("CLS");
					cout << "Questao 12 - Leia uma matriz de tamanho 10x3 com as notas de 10 alunos em tres provas. Em seguida, calcule e escreva na tela o numero de alunos cuja pior nota foi na prova 1, o numero de alunos cuja a pior nota foi na prova 2 e o numero de alunos cuja pior nota foi na prova 3.\n" << endl; // Questionário
					// Código

					int matriz[10][3];

					cout << "	-- Digite os valores para a Matriz [10][3] --\n" << endl;
					criarMatriz10(matriz);

					cout << "\n";

					cout << "	-- Matriz [10][3] --\n" << endl;
					imprimirMatriz10(matriz);

					cout << "\n";

					cout << "-- Menores valores de cada coluna da Matriz [10][3] salvas no vetor [3] --\n" << endl;
					consultaColunas10(matriz);

					system("PAUSE");
					system("CLS");
					break;
				}
				case 13: {
					system("CLS");
					cout << "Questao 13 - Calcular e imprimir na tela uma matriz de tamanho 10x10, em que seus elementos estao na forma:\n\nA[i][j] = 2i + 7j – 2 se i < j\nA[i][j] = 3i2 - 1 se i = j\nA[i][j] = 4i3 + 5j2 + 1 se i > j\n" << endl; // Questionário
					// Código

					int matriz[10][10];

					cout << " Dadas as condicoes de criacao da Matriz [10][10]:\n\n 1. A[i][j] = 2i + 7j – 2 se i < j\n 2. A[i][j] = 3i2 - 1 se i = j\n 3. A[i][j] = 4i3 + 5j2 + 1 se i > j\n\n";
					condicaoMatriz10(matriz);

					cout << "\n	-- Matriz [10][3] --\n\n" << endl;
					respostaMatriz10(matriz);

					system("PAUSE");
					system("CLS");
					break;
				}
				case 14: {
					system("CLS");
					cout << "Questao 14 - Faca um programa que permita ao usuario entrar com um matriz de tamanho 3x3 de numeros inteiros. Em seguida, calcule um vetor contendo tres posicoes, em que cada posicao devera armazenar a soma dos numeros de cada coluna da matriz. Exiba na tela esse array.\n" << endl; // Questionário
					// Código

					int matriz[3][3];

					cout << "	-- Digite os valores para a Matriz [3][3] --\n" << endl;
					criarMatriz(matriz);

					cout << "\n";

					cout << "	-- Matriz [3][3] --\n" << endl;
					imprimirMatriz(matriz);

					cout << "\n";

					cout << "-- Soma das colunas da Matriz [3][3] salva no Vetor [3] --\n" << endl;
					somaColunas(matriz);

					system("PAUSE");
					system("CLS");
					break;
				}
				default: {
					cout << "\nOpcao Invalida!\n" << endl;
					system("pause");
					system("CLS");
					break;
				}
				}

			} while (op2 != 00);

			system("pause");
			system("CLS");
			break;

		default:
			cout << "\nOpcao Invalida!\n" << endl;
			system("pause");
			system("CLS");
			break;
		}
	} while (op != 0);

	system("pause");
	return 0;
}