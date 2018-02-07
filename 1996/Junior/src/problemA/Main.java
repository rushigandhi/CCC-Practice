package problemA;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args){
		
		Scanner in = new Scanner(System.in);
		
		int total = in.nextInt();
		int num;
		
		ArrayList<Integer> numList = new ArrayList<Integer>();
		ArrayList<Integer> sumList = new ArrayList<Integer>();
		
		for (int x = 0; x < total; x++){
			
			num = in.nextInt();
			
			numList.add(num);
			
			int sum = 0;
			
			for (int i = 1; i < num; i++){
				
				if ((num%i) == 0){
					
					sum = sum + i;
					
				}
			}
			
			sumList.add(sum);
		}
		
		for (int j = 0; j < sumList.size(); j++){
			
			if(sumList.get(j) > numList.get(j)){
			
			System.out.println(numList.get(j) + " is an abundant number.");
		}
			
		else if (sumList.get(j) == numList.get(j)){
			
			System.out.println(numList.get(j) + " is a perfect number.");
		}
		
		else {
			System.out.println(numList.get(j) + " is a deficient number.");
		}
		
	}
		
	}

}
