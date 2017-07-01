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
				
				for (int a = 0; a < symbols.length; a++){
				
				if(numOne.charAt(i)==(symbols[a].charAt(0))){
					first = first + symbols[a].charAt(1);
				}
				}
				
			}
			
			for(int c = 0; c < numTwo.length(); c++){
				
				for (int b = 0; b < symbols.length; b++){
					
					if(numOne.charAt(c)==(symbols[b].charAt(0))){
						first = first + symbols[b].charAt(1);
					}
					}
			}
				output.add(first + " " + second);
				
			}
			
			
		
		
		for (int j = 0; j < input.size(); j++){
			
			System.out.println(input.get(j) + output.get(j));
			
		}
}
}
