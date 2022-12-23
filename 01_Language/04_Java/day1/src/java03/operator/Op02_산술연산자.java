package java03.operator;

public class Op02_산술연산자 {
	public static void main(String[] args) {
		int a = 10;
		int b = 6;
		
		System.out.println(a+b);
		System.out.println(a-b);
		System.out.println(a*b);
		System.out.println(a/b); // 몫 (파이썬의 //와 같음)
		System.out.println(a%b); // 나머지
		
		System.out.println(a/(double)b); // 정수와 실수 -> 실수
		System.out.println((double)a/b);
		System.out.println((double)(a/b));
	}
}
