package java04.control;

public class Loop01 {
	public static void main(String[] args) {
		//for (초기화;조건식;증감식){반복내용}
		//조건식을 비워두면 항상 참으로 인식해서 끝나지 않음
		//반복횟수를 알고 있을 떄 사용하면 좋음
		
		for(int i = 0 ; i<10; i++) {
			System.out.println(i);
		}
		
		for(int i = 0, j = 10; i < 10 ; i += 2, j--) {
			System.out.println(i);
			System.out.println(j);
		}
		
		//중첩 반복문 (구구단)
		for(int i = 2; i<=9; i++) {
			System.out.printf("%d단\n", i);
			for(int j = 1; j<=9; j++) {
				System.out.printf("%d * %d = %d\n", i, j, i * j);
			}
		}
		//print, printf 자동으로 줄이 바뀌지 않음을 항상 생각하자!
	}
}
