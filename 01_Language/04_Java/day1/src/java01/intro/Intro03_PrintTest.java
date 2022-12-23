package java01.intro;

public class Intro03_PrintTest {
	public static void main(String[] args) {
		//print 를 써보자
		System.out.print("Hello Word!! \n");
		// \n : 줄 바꿈, 파이썬과 동일
		
		// println을 써보자
		// sysout + ctrl + space 하면 자동완성해줌
		System.out.println("Hello World!!");
		System.out.println("Hello World!!");
		
		System.out.println("\\"); // 두개를 써야지 \ 가 출력됨
		System.out.println("\"");  // "
		
		System.out.printf("%d \n", 10); //정수 (10진수)
		System.out.printf("%o \n", 10); //정수 (8진수)
		System.out.printf("%X \n", 10); //정수 (16진수)
		System.out.printf("%x \n", 10); //정수 (16진수)
		
		System.out.printf("%4d\n \n", 10); // 4칸을 확보한 뒤 오른쪽부터 차지
		System.out.printf("%-4d\n \n", 10); // 4칸을 확보한 뒤 왼쪽부터 차지
		System.out.printf("%04d\n \n", 10); // 4칸을 확보한 뒤 오른부터 차지(빈칸을 0을 채움)
		
		System.out.printf("%f\n", 10.1); //실수
		System.out.printf("%.2f\n", 10.1); //실수 (소수점 둘째자리까지)
		
		System.out.printf("%s\n", "Vailish");
		System.out.printf("%c\n", 'o');
		
		System.out.printf("안녕하세요. 저는 %s입니다. 제 혈애액형은 %c일껄요?", "Vailish", 'C');
		
		// 파이썬과는 다르게 println은 한개의 인자만 받을 수 있다.
		// System.out.pirntln(a, b)처럼 못씀
		// 이렇게 쓰려면 System.out.println(a + " " + b) 처럼 쓰거나
		// System.out.printf("%d %d%n", a, b)와 같이 사용해야함
	}
}
