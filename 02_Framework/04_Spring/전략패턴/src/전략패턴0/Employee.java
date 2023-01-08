package ��������0;

public class Employee extends Person{
	
	//������ : ��ü����������, Ÿ��������
	//��ü���������� : IoC�����ν� Ż�� ����.
	//Ÿ�������� : Interface�� Ȱ�������ν� �����Ѱ������ν� �ؼҰ���.
	//			   �Ʒ��� ���ÿ��� DoWork�ڸ��� �������̽��� ��������ν� �پ��� �༮���� �־��� �� ����
	
//	private DoWork work = new DoWork(); //new�� ���Ⱑ �ƴ� test���� ����ϰԲ� ����(IoC)
	private DoWork work;
	private EatWellStory wellStory = new EatWellStory();
	//��ü�� �־��ִ� ������� Constructor Injection, Property Injection �̷��� �� ���� ����� �ִ�.
	//�����ڿ� ��ü�� �־��ָ� Constructor Injection
	public Employee(DoWork work) {
		this.work = work;
	}
	//�����ڿ� ��ü�� �־��ָ� Property Injection/Setter Injection
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
