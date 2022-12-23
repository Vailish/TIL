package java03.operator;

public class Op05_삼항연산자 {
	public static void main(String[] args) {
		//조건식 ? 식1(true) : 식2(false)
		int num = (int)(Math.random()*10)+1;
		
		System.out.println("출력합니다~");
		System.out.println(num % 2 == 0 ? "짝" : "홀"); // ? 뒤에 참 거짓 값 있어야함
	}
}
