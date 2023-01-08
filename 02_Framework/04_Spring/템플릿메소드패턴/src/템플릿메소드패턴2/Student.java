package 템플릿메소드패턴2;

public class Student extends Person{

	@Override
	protected void doSomething() {
		// TODO Auto-generated method stub
		System.out.println("공부를 한다.");
		System.out.println("급식을 먹는다.");
	}

}
