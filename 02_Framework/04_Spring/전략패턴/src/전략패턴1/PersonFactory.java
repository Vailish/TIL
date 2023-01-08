package 전략패턴1;
//스프링 컨테이너 이전에는 PersonFactory라는 것을 만들어서 생성을 했었음...
//이것이 팩토리 패턴
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
