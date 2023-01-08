package 전략패턴1;

public class Person {
	private String name;
	private DoSomething doSomething;
	private Eating eating;
	public void setDoSomething(DoSomething doSomething) {
		this.doSomething = doSomething;
	}
	public void setEating(Eating eating) {
		this.eating = eating;
	}
	
	public void daily() {
		System.out.println("입실체크를 한다.");
		doSomething.doSomething();
		eating.eat();
		System.out.println("퇴실체크를 한다.");
	}
}
