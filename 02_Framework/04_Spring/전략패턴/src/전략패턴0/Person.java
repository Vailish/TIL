package 전략패턴0;

public abstract class Person {
	private String name;
	public abstract void doSomething();
	public void daily() {
		System.out.println("입실체크를 한다.");
		doSomething();
		System.out.println("퇴실체크를 한다.");
	}
}
