package 템플릿메소드패턴1;

public class Employee extends Person{

	@Override
	public void doSomething() {
		// TODO Auto-generated method stub
		System.out.println("출근한다.");
		System.out.println("소와 같이 일을 한다.");
		System.out.println("웰스토리를 먹는다.");
		System.out.println("퇴실체크한다.");
	}

}
