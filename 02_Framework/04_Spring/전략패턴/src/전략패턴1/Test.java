package ��������1;

public class Test {
	public static void main(String[] args) {
//		DoWork work = new DoWork();
//		DoStudy study = new DoStudy();
//		EatWellStory wellStory = new EatWellStory();
//		EatCafeteria cafeteria = new EatCafeteria();
//		//Employee
//		Person employee = new Person();
//		employee.setDoSomething(work);
//		employee.setEating(cafeteria);
//		Person student = new Person();
//		student.setDoSomething(study);
//		student.setEating(cafeteria);
//		Person dev = new Person();
//		dev.setDoSomething(study);
//		dev.setEating(wellStory);
		
		//PersonFactory ����ϱ�
		Person employee = PersonFactory.getInstance("Employee");
	}
}
