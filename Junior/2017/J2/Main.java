//package J2;

import java.util.Scanner;

public class Main {
	
	public static void main(String[] args){
		
		Scanner in = new Scanner(System.in);
		
		int num = in.nextInt();
		
		int times = in.nextInt();
		
		String number = String.valueOf(num);
		
		
		for (int x = 0; x < times; x++){
		
			number = number + "0";
			
			num = num + Integer.parseInt(number);
			

		}
		
		System.out.println(num);
		
		
	}

}
