package java04.control;

public class IF01 {
	public static void main(String[] args) {
		//if(조건식) {} 조건식이 참일 경우 블록 내부 수행
		
		int n = 5;
		
		if(n < 10 ) //수행할 문장이 한 문장이라면 중괄호 생략 가능
			System.out.println("해당 문장을 수행");
			System.out.println("해당 문장을 수행2");
			// 얘는 if 안이 아니라 if 블록 밖임, 그래서 되도록 생략하지말자
			// 파이썬과 다르게 띄어쓰기로 나누지 않기 때문
	}
}
