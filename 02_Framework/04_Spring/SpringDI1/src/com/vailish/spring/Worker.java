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
		System.out.println(this.computer.getInfo() + " �� ���մϴ�.");
	}
	public void setHong(int value) {
		
	}
}
