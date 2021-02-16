// Biblioteca da lista de Vetor e Matriz
#include <iostream>

using namespace std;

int criarVetor(int vet[10], int &valorMaior, int &valorMenor) {

	int i;

	for (i = 0; i < 10; i++) {
		cout << "Digite o valor para a posicao [" << i << "] aqui: ";
		cin >> vet[i];
	}

	cout << "\n";

	/*
	for (i = 0; i < 10; i++) {
		cout << "O valor na posicao [" << i << "] e: " << vet[i] << endl;
	}

	cout << "\n";
	*/

	valorMaior = vet[0];
	valorMenor = vet[0];

	for (i = 0; i < 10; i++) {

		if (valorMaior < vet[i]) {
			valorMaior = vet[i];
		}

		if (valorMenor > vet[i]) {
			valorMenor = vet[i];
		}

	}

	return 0;
}


void numeroImpar(int vet[10], int valor) {

	int cont = 0;

	for (int i = 0; i < 10; i++) {

		if ((vet[i] % 2) != 0) {
			cout << "Numero impar:. Posicao: [" << i << "], Valor: [" << vet[i] << "]" << endl;
		}
		else {
			cont++;
		}

		if (cont == 10) {
			cout << "Nenhum valor impar encontrado!" << endl;
		}
	}

}


void consultarVetor(int vet[10], int valor) {

	int i, cont;
	i = cont = 0;

	cin >> valor;
	cout << "\n";

	for (i = 0; i < 10; i++) {
		if (vet[i] == valor) {
			cout << "Posicao: [" << i << "], Valor: [" << vet[i] << "]" << endl;
		}
		else {
			cont++;
		}
	}

	if (cont == 10){
		cout << "Numero nao existe!" << endl;
	}

}


void criaConsulta(int vet[10], int &valor) {

	int i, j, posicao;
	posicao = valor = i = j = 0;

	for (i = 0; i < 10; i++) {
		cout << "Digite o valor para a posicao [" << i << "] aqui: ";
		cin >> vet[i];

		for (int j = 0; j < i; j++) {
			if (vet[i] == vet[j]) {
				do {
					cout << "Valor ja existe no vetor, na posicao: [" << j << "]!\n\nPor favor digite outro valor: ";
					cin >> vet[i];
				} while (vet[i] == vet[j]);
			}

		}

	}

	cout << "\n\n";

}



void mostrarVetor(int vet[10]) {

	for (int i = 0; i < 10; i++) {
		cout << "Posicao: [" << i << "], Valor: [" << vet[i] << "]" << endl;
	}
}


void consultaPrimo(int vet[10]) {

	int aux = 0;

	for (int i = 0; i < 10; i++) {

		int num, cont = 1;
		num = 0;

		do {

			cont++;

		} while (((vet[i] % cont) != 0) && ((cont*cont) <= vet[i]));

		if (vet[i] == 2) {
			cout << "O numero: [" << vet[i] << "] que esta na posicao: [" << i << "] e primo." << endl;
		}

		if (vet[i] == 1 || vet[i] % cont == 0) {
			aux++;
		}
		else {
			cout << "O numero: [" << vet[i] << "] que esta na posicao: [" << i << "] e primo." << endl;
		}

		if (aux >=10) {
			cout << "Nao existe nenhum numero primo no vetor!" << endl;
		}

	}

	cout << "\n" << endl;

}


int criarMatriz(int matriz[3][3]) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 3; i++) {

		for (j = 0; j < 3; j++) {

			cout << "Inserir o valor da linha [" << i << "] e coluna [" << j << "]: ";
			cin >> matriz[i][j];
		}

		cout << "\n";
	}
	return 0;
}


void imprimirMatriz(int matriz[3][3]) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 3; i++) {

		for (j = 0; j < 3; j++) {
			cout << "	" << matriz[i][j] << " ";
		}

		cout << "\n";
	}

	cout << "\n";

}


void multiplicadorMatriz(int matriz[3][3], int multiplicador) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 3; i++) {

		for (j = 0; j < 3; j++) {

			matriz[i][j] *= multiplicador;

		}

	}

}


int criarMatriz2(int matriz[2][3]) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 2; i++) {

		for (j = 0; j < 3; j++) {

			cout << "Inserir o valor da linha [" << i << "] e coluna [" << j << "]: ";
			cin >> matriz[i][j];
		}

		cout << "\n";
	}
	return 0;
}


void imprimirMatriz2(int matriz[2][3]) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 2; i++) {

		for (j = 0; j < 3; j++) {
			cout << "	" << matriz[i][j] << " ";
		}

		cout << "\n";
	}

	cout << "\n";

}


int somadorMatriz2(int matriz[2][3]) {

	int i, j, somador;
	somador = i = j = 0;

	for (i = 0; i < 2; i++) {

		for (j = 0; j < 3; j++) {

			somador += matriz[i][j];

		}

	}
	return somador;

}


int criarMatriz4(int matriz[4][4]) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 4; i++) {

		for (j = 0; j < 4; j++) {

			cout << "Inserir o valor da linha [" << i << "] e coluna [" << j << "]: ";
			cin >> matriz[i][j];
		}

		cout << "\n";
	}
	return 0;
}


void imprimirDiagonal4(int matriz[4][4]) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 4; i++) {

		for (j = 0; j < 4; j++) {

			if (i == j) {
				cout << "	[" << matriz[i][j] << "] ";
			}
			else if (i != j) {
				cout << "	" << matriz[i][j] << " ";
			}

		}

		cout << "\n";
	}

	cout << "\n\nDiagonal principal: ";

	for (i = 0; i < 4; i++) {

		for (j = 0; j < 4; j++) {

			if (i == j) {
				cout << "[" << matriz[i][j] << "] ";
			}

		}

	}

	cout << "\n\n";

}


void ocultarDiagonal(int matriz[3][3]) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 3; i++) {

		for (j = 0; j < 3; j++) {

			if (i == j) {
				cout << "	";
			}
			else if (i != j) {
				cout << "	" << matriz[i][j] << " ";
			}

		}

		cout << "\n";
	}

	cout << "\n\nElementos da diagonal principal que foram ocultos: ";

	for (i = 0; i < 3; i++) {

		for (j = 0; j < 3; j++) {

			if (i == j) {
				cout << "[" << matriz[i][j] << "] ";
			}

		}

	}

	cout << "\n\n";

}


void somaColunas(int matriz[3][3]) {

	int vet[3];
	int i, j, posicao_a, posicao_b, posicao_c;
	posicao_a = posicao_b = posicao_c = i = j = 0;

	for (i = 0; i < 3; i++) {

		for (j = 0; j < 3; j++) {

			if (j == 0) {
				posicao_a += matriz[i][j];
			}
			if (j == 1) {
				posicao_b += matriz[i][j];
			}
			if (j == 2) {
				posicao_c += matriz[i][j];
			}

		}

	}

	for (i = 0; i < 3; i++) {

		if (i == 0) {
			vet[i] = posicao_a;
		}
		if (i == 1) {
			vet[i] = posicao_b;
		}
		if (i == 2) {
			vet[i] = posicao_c;
		}

	}

	cout << "	";

	for (i = 0; i < 3; i++) {
		cout << "[" << vet[i] << "]	";
	}

	cout << "\n\n";

}


int criarMatriz10(int matriz[10][3]) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 10; i++) {

		for (j = 0; j < 3; j++) {

			cout << "Inserir o valor da linha [" << i << "] e coluna [" << j << "]: ";
			cin >> matriz[i][j];
		}

		cout << "\n";
	}
	return 0;
}


void imprimirMatriz10(int matriz[10][3]) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 10; i++) {

		for (j = 0; j < 3; j++) {
			cout << "	" << matriz[i][j] << " ";
		}

		cout << "\n";
	}

	cout << "\n";

}


void consultaColunas10(int matriz[10][3]) {

	int vet[3];
	int i, j, posicao_a, posicao_b, posicao_c;
	posicao_a = posicao_b = posicao_c = i = j = 0;

	posicao_a = matriz[0][0];
	posicao_b = matriz[0][1];
	posicao_c = matriz[0][2];

	for (i = 1; i < 10; i++) {

		for (j = 0; j < 3; j++) {

			if (j == 0) {
				if (matriz[i][j] < posicao_a) {
					posicao_a = matriz[i][j];
				}

			}
			if (j == 1) {
				if (matriz[i][j] < posicao_b) {
					posicao_b = matriz[i][j];
				}
			}
			if (j == 2) {
				if (matriz[i][j] < posicao_c) {
					posicao_c = matriz[i][j];
				}
			}

		}

	}

	for (i = 0; i < 3; i++) {

		if (i == 0) {
			vet[i] = posicao_a;
		}
		if (i == 1) {
			vet[i] = posicao_b;
		}
		if (i == 2) {
			vet[i] = posicao_c;
		}

	}

	cout << "	";

	for (i = 0; i < 3; i++) {
		cout << "[" << vet[i] << "]	";
	}

	cout << "\n\n";

}


int condicaoMatriz10(int matriz[10][10]) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 10; i++) {

		for (j = 0; j < 10; j++) {

			if (i < j) {
				matriz[i][j] = (((2 * i) + (7 * j)) - 2);
			}

			if (i == j) {
				matriz[i][j] = ((3 * i * 2) - 1);
			}

			if (i > j) {
				matriz[i][j] = (((4 * i * 3) + (5 * j * 2)) + 1);
			}

		}

	}
	return 0;
}


void respostaMatriz10(int matriz[10][10]) {

	int i, j;
	i = j = 0;

	for (i = 0; i < 10; i++) {

		for (j = 0; j < 10; j++) {
			cout << "	" << matriz[i][j] << " ";
		}

		cout << "\n";
	}

	cout << "\n\n";

}