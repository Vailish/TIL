package com.vailish.spring;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

//Ŭ���� ù���ڸ� �ҹ��ڷ� �ٲ� �̸��� bean�� �̸��� ��!
@Component
public class Worker {
	//���α���... reflection
	//�ʵ� �������� ������ : ��ȯ���������� ����� �ֱ� ����
	@Autowired //                                          1. �ʵ� ������
	private Computer computer; //������ ���� ����
//	@Autowired //(Spring ����, constructor injection)
//	public Worker(Computer computer) {
////		computer = new Desktop(); //                   2. constructor ������
//		this.computer = computer;
////		System.out.println("Worker�� �����ڰ� �ҷȽ��ϴ�");
//	}
	//�ڵ����� Ÿ���� ��ġ�ϴ� bean�� ã�ƴٰ� ���⿡ �־���(��κ��� ��Ȳ)
	//�� �� �̻��̸� ������ ��
	//������ ������������ �ϳ��� ���� �ڽŰ� �̸��� ���ٸ� �׳༮�� ����������
//	@Autowired
//	@Qualifier("desktop") //�̷��� �̸��� ��� �ص���
//	public void setComputer(Computer computer) { //        3. property ������
//		this.computer = computer;
//	}

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
