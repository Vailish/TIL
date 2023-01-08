package 전략패턴0;

public class Dev extends Person{
	private DoStudy study;
	private EatWellStory wellStory;
	@Override
	public void doSomething() {
		// TODO Auto-generated method stub
		study.doSomething();
		wellStory.doSomething();
	}
}
