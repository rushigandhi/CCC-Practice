package problemD;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
public static void main(String[] args){
		
		Scanner in = new Scanner(System.in);
		int total = in.nextInt();
		
		ArrayList<String> input = new ArrayList<String>();
		ArrayList<String> output = new ArrayList<String>();
		
		char[] symbols = { 'I', 'V', 'X', 'L', 'C', 'D', 'M'};
		int[] nums = { 1, 5, 10, 50, 100, 500, 1000};
		
		for(int x = 0; x < total; x++){
			
			in.nextLine();
			String equation = in.nextLine();
			input.add(equation);
			
			String numOne = equation.substring(0, equation.indexOf("+"));
			String numTwo = equation.substring(equation.indexOf("+") + 1, equation.indexOf("="));
			int first = 0;
			int second = 0;
			for(int i = 0; i < numOne.length(); i++){
				
				for (int a = 0; a < 7; a++){
				
				if(numOne.charAt(i)==symbols[a]){
					first = first + nums[a];
				}
				}
				
			}
				for(int k = 0; k < numTwo.length(); k++){
				
				for (int b = 0; b < 7; b++){
				
				if(numTwo.charAt(k)==symbols[b]){
					second = second + nums[b];
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
