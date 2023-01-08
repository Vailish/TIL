package ��������1;
//������ �����̳� �������� PersonFactory��� ���� ���� ������ �߾���...
//�̰��� ���丮 ����
public class PersonFactory {
	static DoSomething work = new DoWork();
	static DoSomething study = new DoStudy();
	static Eating cafeteria = new EatCafeteria();
	static Eating wellStory = new EatWellStory();
	
	public static Person getInstance(String type) {
		Person p = new Person();
		switch (type) {
		case "Employee":
			p.setDoSomething(work);
			p.setEating(wellStory);
			break;

		case "Student":
			p.setDoSomething(study);
			p.setEating(cafeteria);
			break;
		case "dev":
			p.setDoSomething(study);
			p.setEating(wellStory);
			break;
		}
		return p;
	}
}
