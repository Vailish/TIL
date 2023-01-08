package 전략패턴0;

public class Employee extends Person{
	
	//의존성 : 객체생성의존성, 타입의존성
	//객체생성의존성 : IoC함으로써 탈출 가능.
	//타입의존성 : Interface를 활용함으로써 느슨한결합으로써 해소가능.
	//			   아래의 예시에서 DoWork자리에 인터페이스를 사용함으로써 다양한 녀석들을 넣어줄 수 있음
	
//	private DoWork work = new DoWork(); //new를 여기가 아닌 test에서 사용하게끔 변경(IoC)
	private DoWork work;
	private EatWellStory wellStory = new EatWellStory();
	//객체를 넣어주는 방법에는 Constructor Injection, Property Injection 이렇게 두 가지 방법이 있다.
	//생성자에 객체를 넣어주면 Constructor Injection
	public Employee(DoWork work) {
		this.work = work;
	}
	//설정자에 객체를 넣어주면 Property Injection/Setter Injection
	public void setEatWellStory(EatWellStory wellSotry) {
		this.wellStory = wellStory;
	}
	@Override
	public void doSomething() {
		// TODO Auto-generated method stub
		work.doSomething();
		wellStory.doSomething();
	}

}
