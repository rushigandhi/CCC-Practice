package problemC;

import java.util.ArrayList;
import java.util.Scanner;


public class Main {
public static void main(String[] args){
		
		Scanner in = new Scanner(System.in);
		int total = in.nextInt();
		ArrayList<Integer> nList = new ArrayList<Integer>();
		ArrayList<Integer> kList = new ArrayList<Integer>();
		int totalNum = 0;
		
		for (int x = 0; x < total; x++){
			
			nList.add(in.nextInt());
			kList.add(in.nextInt());
			
		}
		
		for (int i = 0; i < nList.size(); i++){
			String pattern = "";
			
			for (int j = 0; j < kList.get(i); j++){
			pattern = pattern + "1";
			}
			for (int a = 0; a < nList.get(i)-kList.get(i); a++){
				pattern = pattern + "0";
				}
			System.out.println(pattern);
		
			while(!(pattern.lastIndexOf("10")==-1)){
				pattern = pattern.replaceFirst("10", "01");
				System.out.println(pattern);
			}
		}
		
		
}

}