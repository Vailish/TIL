package com.vailish.spring;

public class Worker {
	private Computer computer; //������ ���� ����
//	public static Worker getinstance() {
//		return new Worker();
//		// �̷������� ����Ϸ��� applicationContext���� id �տ� factory-method="getInstance"�� ����ص� ��. ���� �Ⱦ�
//		
//	}
	public Worker() {
//		computer = new Desktop();
		System.out.println("Worker�� �����ڰ� �ҷȽ��ϴ�");
	}
	public void setComputer(Computer computer) {
		this.computer = computer;
	}
	public void doWork() {
		System.out.println(this.computer.getInfo() + " �� ���մϴ�." + this.age);
	}
	private int age;
	public void setHong(int value) {//applicationContext���� ������� value, ��ü���� ref ���
		this.age = value;		
	}
	//�ڹ��ڵ带 �ǵ帮�� �ʰ� ����(applicationContext�� �̿��ؼ� ������� ������ �� �ִ�.
	//ex) worker�� ����ũž���� ������ ��Ʈ������ ������ ��� ������ ������
}
