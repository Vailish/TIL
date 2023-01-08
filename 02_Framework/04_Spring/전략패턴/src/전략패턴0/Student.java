package 전략패턴0;

public class Student extends Person{
	private DoStudy study= new DoStudy();
	private EatCafeteria cafeteria = new EatCafeteria();
	@Override
	public void doSomething() {
		// TODO Auto-generated method stub
		study.doSomething();
		cafeteria.doSomething();
	}

}
