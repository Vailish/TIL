package 템플릿메소드패턴2;

public abstract class Person {
	private String name;
	
	protected abstract void doSomething(); // 동적 바인딩, 이런경우에는 private여도 상관없다. - 안됨...protected는 가능!
	
	public void daily() {
		System.out.println("입실체크한다.");
		doSomething(); //중복되는 부분은 따로 정의해주고,
		               //다른 부분만 추상으로 넣어줘서 처리해주는 것을 템플릿메소드패턴이라고 함!
		System.out.println("퇴실체크한다.");
	}
}
