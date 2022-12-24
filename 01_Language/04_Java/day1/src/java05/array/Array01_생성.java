package java05.array;

public class Array01_생성 {
	public static void main(String[] args) {
		
		//1차원 배열을 선언하는 방법
		int[] score1; // 앞으로 이것으로 사용할 것
		int score2[];
		
//		score1 = {1, 2, 3, 4, 5}; // 이렇게는 작성 불가, 쓰고 싶으면 생성과 함께 써야함
		score1 = new int[] {1, 2, 3, 4, 5};
		
		int[] score3 = {1, 2, 3, 4, 5};
		System.out.println(score3);
		
		int[] score4 = new int[5];
		 
		score4[0] = 10;
		score4[1] = 20;
		score4[2] = 30;
		score4[3] = 40;
		
		for(int i = 0 ; i<score4.length; i++) {
			System.out.println(score4[i]);  // score4[4] 는 기본값인 0이 들어가있음
		}
	}
}
