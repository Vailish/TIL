package java02.variable;

public class Var01_VariableTest {
	public static void main(String[] args) {
		int a;  // 선언
		a = 10; // 저장
		System.out.println(a); // 변수는 값을 할당하지 않고서 사용할 수 없음
		int b = 20;
		System.out.println(b);
		int c = a; // 오른쪽 변수의 값을 꺼내서 왼쪽 변수에 담음
		System.out.println(c);
		c = b;
		System.out.println(c);
		
		System.out.printf("변수 c의 값은 %d", c);
	}
}
