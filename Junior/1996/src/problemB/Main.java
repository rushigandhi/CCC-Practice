package problemB;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	
@SuppressWarnings("resource")
public static void main(String[] args){
		
		Scanner in = new Scanner(System.in);
		
		int total = in.nextInt();
		long newNum = 0;
		ArrayList<Long> list = new ArrayList<Long>();

		for (int x = 0; x < total; x++){
			long num = in.nextLong();
			list.add(num);
			
		}
		
		for (int i = 0; i < list.size(); i++){
 
			System.out.println(list.get(i));
			
			String line = Long.toString(list.get(i));
			
			int length = line.length();
			
			while (length!=2){
				length--;
				String sub = line.substring(line.length()-1);
				line = line.substring(0, line.length()-1);
				String newLine = line.substring(0);
				newNum = Long.parseLong(newLine) - Long.parseLong(sub);
				line = Long.toString(newNum);
				System.out.println(line);
				
				
			}
			
			if(newNum%11==0){
				System.out.println("The number " + list.get(i) + " is divisible be 11");
			}
			
			
			System.out.println();
			

		}

}
}
