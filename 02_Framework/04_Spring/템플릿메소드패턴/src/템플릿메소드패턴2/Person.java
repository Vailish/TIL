package ���ø��޼ҵ�����2;

public abstract class Person {
	private String name;
	
	protected abstract void doSomething(); // ���� ���ε�, �̷���쿡�� private���� �������. - �ȵ�...protected�� ����!
	
	public void daily() {
		System.out.println("�Խ�üũ�Ѵ�.");
		doSomething(); //�ߺ��Ǵ� �κ��� ���� �������ְ�,
		               //�ٸ� �κи� �߻����� �־��༭ ó�����ִ� ���� ���ø��޼ҵ������̶�� ��!
		System.out.println("���üũ�Ѵ�.");
	}
}
