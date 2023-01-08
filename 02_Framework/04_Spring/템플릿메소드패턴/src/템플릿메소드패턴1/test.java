package 템플릿메소드패턴1;

public class test {
	//Employee와 Student가 Person이라는 공통구조를 가짐으로써 같은 타입으로 처리가 가능
	//같은 타입으로 처리가 가능
	
	public static void main(String[] args) {
		Person p1 = new Employee();
		Person p2 = new Student();
		p1.doSomething();
		
		p2.doSomething();
		
	}
}
