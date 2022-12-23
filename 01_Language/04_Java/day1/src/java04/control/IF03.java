package java04.control;

public class IF03 {
	public static void main(String[] args) {
		//if(조건식) {} 조건식이 참일 경우 if블록 내부 수행/ 거짓이면 else 블록 수행
		int score = 87;
		
		//이상 초과 이하 미만
		
		// 90점 이상 일 경우는 A학점
		// 90점 미만 80점 이상 일 경우는 B학점
		// 80점 미만 70점 이상 일 경우는 C학점
		// 그 외 F학점
//		if(score > 90) {
//			System.out.println("A");
//		} else {
//			if(score < 90 && score>80) {
//				System.out.println("B");
//			} else {
//				if(score < 80 && score >= 70) {
//					System.out.println("C");
//				} else {
//					System.out.println("F");
//				}
//			}
//		}
		
		if(score > 90) // 하나면 생략 가능하므로, 아래와 같이 되는 것! 파이썬과 모양 비슷해짐..
			System.out.println("A");
		else if (score>80)
			System.out.println("B");
	    else if (score >= 70) 
			System.out.println("C");
		else
			System.out.println("F");

	}
}
