package class02;

import java.util.Random;

public class FuntionTest4 {
	public static void main(String[] args) {
		boolean homework;
		
		System.out.println("아침에 일어난다.");
		moves("회사", "대중교통");
		homework = works();
		moves("집", "대중교통");
		
		if (homework)
			System.out.println("과제를 해결한다.");
		
		System.out.println("잔다.");
		
		System.out.println("===========================");
		
		System.out.println("아침에 일어난다.");
		System.out.println("아침밥을 먹는다.");		
		moves("제주도", "비행기");
		homework = works();
		moves("집", "배");

		if (homework)
			System.out.println("과제를 해결한다.");
		
		System.out.println("잔다.");
	}
	
	public static boolean works() {  // void : 반환값이 없다라는 뜻
		System.out.println("오전 업무를 한다");
		System.out.println("점심을 먹는다");
		System.out.println("오후 업무를 한다");
		//과제 랜덤 발생기.
		Random random = new Random();
		return random.nextBoolean();
	}
	
	public static void moves(String place, String vehicle) {
		System.out.println(place+"(으)로" +vehicle +"(을)를 이용하여 이동한다.");
	}
}
