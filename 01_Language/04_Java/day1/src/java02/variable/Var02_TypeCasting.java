package java02.variable;

public class Var02_TypeCasting {
	public static void main(String[] args) {
		int a = 10;
		int b = a;
		System.out.printf("a : %d \n", a);
		System.out.printf("b : %d \n", b);
		
		a = 12;
		// b는 안바뀜
		System.out.printf("a : %d \n", a);
		System.out.printf("b : %d \n", b);
		
		// 작은집에서 큰집으로 이사갈때는 문제가 없음(묵시적)
		short sa = 32767;
		int c = sa;
		// 큰집에서 작은집으로 갈때는 컨펌이 필요(명시적)
		short sb = (short) c;
		
		float f = 10;
		// 같은 크기의 집이라도 컨펌이 필요한 경우(명시적)
		int g = (int) f;
		
		System.out.println(sa + " " + sb);
		System.out.printf("%d %d%n", sa, sb);
	}
}
