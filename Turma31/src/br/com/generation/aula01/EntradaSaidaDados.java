package br.com.generation.aula01;

import java.util.Scanner;

public class EntradaSaidaDados {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
			Scanner entrada = new Scanner(System.in);
			
			int a, b, soma;
			
			System.out.println("Escreva o valor de a: ");
			a = entrada.nextInt();
			
			System.out.println("Escreva o valor de b:");
			b = entrada.nextInt();
			
			soma = a + b;
			
			System.out.println("A soma de A com B: " + soma);
			
			entrada.close();
	}

}
