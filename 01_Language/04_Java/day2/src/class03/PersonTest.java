package class03;

public class PersonTest {
	public static void main(String[] args) {
		Person p1 = new Person();  // 같은 패키지 내에서는 import없이 가져다 쓸 수 있음
		
		p1.name = "Yang";
		p1.age = 45;
		p1.hobby = "youtube";
		
		Person p2 = new Person();
		
		p2.name = "Hong";
		p2.age = 25;
		p2.hobby = "Golf";
		
		
		System.out.println(p1);
		System.out.println(Person.personCount);
		System.out.println(p1.personCount); // 밑줄은 클래스 메모리에 있으니 윗줄 처럼 쓰고 heap에서 인스턴스를 거치지 말고 Person.으로 접근하라는 뜻
		
		Person p = new Person();
		p.study((byte) 10);
		p.study((short) 10);
		p.study(10);
		p.study(10L);  // O 메소드 오버로딩
//		p.study((10.0f); // X
//		p.study(10.0); // X
//		p.study(10, 10); // X 정의한 것 이외에 사용 불가
	}
}
