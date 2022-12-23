package java03.operator;

public class Op03_비교연산자 {
	public static void main(String[] args) {
		int a = 10;
		
		System.out.println(a > 10);
		System.out.println(a != 10);
		System.out.println(a >= 10);
		
		System.out.println(a == 10);
		System.out.println(a != 10);
		
		String c = "Hi";
		String d = "Hi";
		String e = new String("Hi");
		
		System.out.println(c == d);       // 문자열이 같다면 같은 주소를 가리킴
		System.out.println(c == e);       // new String은 기존 존재여부와 상관없이 무조건 만들어서 주소값이 달라서 false가나옴
		System.out.println(c.equals(e));  // 문자가 같은지 비교할 땐 equals(), 문자열은 파이썬이 편하긴 함
	}
}
