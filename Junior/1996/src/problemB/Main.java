package problemB;

import java.util.Scanner;

public class Main {
	
@SuppressWarnings("resource")
public static void main(String[] args){
		
		Scanner in = new Scanner(System.in);
		
		int total = in.nextInt();

		for (int x = 0; x < total; x++){
			int num = in.nextInt();
 
			System.out.println(num);
			
			String line = Integer.toString(num);
			
			int length = line.length();
			
			for (int i = 0;  i < length; i++){
							
				int sub = Integer.parseInt(line.charAt(line.length()-1) + "");
				
				line = line.substring(0, line.length()-1);
				
				int diff = Integer.parseInt(line) - sub;
				
				line = Integer.toString(diff);
				
				System.out.println(line);
				
			}	
			
		}

}
}
