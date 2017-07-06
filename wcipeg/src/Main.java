import java.util.Scanner;

public class Main {
	
	public static void main (String[] args){
		
		Scanner in = new Scanner(System.in);
		
		double num = in.nextInt() * 1.0;
		
		int counter = 0;
		
		while (num != 1.0){
			
		if (!(num%2.0 == 0))
			num = (3*num) + 1;
		else
			num = num/2.0;
		
		counter++;
		}
		
		System.out.println(counter);	
					
	}

}
