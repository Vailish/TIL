package 전략패턴0;

public class Test {
	public static void main(String[] args) {
		//work에 대한 의존성이 Employee에서 Test로 이관됨.
		//이것이 IoC(제어의 역전)
		DoWork work = new DoWork();
		//Test가 work를 Employee에 넣어줬다
		//이것이 DI(의존성 주입)
		Person p = new Employee(work);
		p.daily();
	}
}
