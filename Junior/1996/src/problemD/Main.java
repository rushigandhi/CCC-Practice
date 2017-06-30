package problemD;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
public static void main(String[] args){
		
		Scanner in = new Scanner(System.in);
		int total = in.nextInt();
		
		ArrayList<String> input = new ArrayList<String>();
		ArrayList<String> output = new ArrayList<String>();
		
		String[] symbols = { "I1", "V5", "X10", "L50", "C100", "D500", "M1000"};
		
		for(int x = 0; x < total; x++){
			
			in.nextLine();
			String equation = in.nextLine();
			input.add(equation);
			
			String numOne = equation.substring(0, equation.indexOf("+"));
			String numTwo = equation.substring(equation.indexOf("+") + 1, equation.indexOf("="));
			int first = 0;
			int second = 0;
			for(int i = 0; i < numOne.length(); i++){
				
				if(numOne.charAt(i)==(symbols[i].charAt(0))){
					first = first + symbols[i].charAt(1);
				}
				
			}
			
			for(int i = 0; i < numTwo.length(); i++){
				
				if(numTwo.charAt(i)==(symbols[i].charAt(0))){
					second = second + symbols[i].charAt(1);
				}
				
				output.add(first + " " + second);
				
			}
			
			
		}
		
		for (int j = 0; j < input.size(); j++){
			
			System.out.println(input.get(j) + output.get(j));
			
		}
}
}
