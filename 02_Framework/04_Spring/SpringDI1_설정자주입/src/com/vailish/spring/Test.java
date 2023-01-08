package com.vailish.spring;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

//���̺� : �����������, ���̺귯������..
//         ������Ʈ ��Ŭ�� > configure > convert to Maven Project
//���̺쿡 ������ ������...
//1. alt + F5 update project. (���� ��Ŭ�� > ���̺� > ������Ʈ ������Ʈ)
//2. ��ܸ޴� project > clean
//3. ��Ŭ���� �� ����, ����� > .m2���� ����(���Ͽ� 1����Ʈ�� �ٸ��� �ȵǴ� ��찡 ����µ� �̰�� ã�� ����Ƿ� ����� �ٽ��Ѽ� �ٽ� ����ָ� ��)

//���̺��� ���ؼ� ������Ʈ�� Spring ���̺귯�� ����
//    https://mvnrepository.com/ > spring �˻�(spring core������ �� �� ������ Ȯ��� Spring context�� ����) > Spring Context
//     > �ٿ�ε���� ����(���������� ���̴� �༮, ���⼭�� 5.3.18) > Maven �����ؼ� pom.xml�� build �ڿ� > <dependencies> �־��ְ�
//     > �� �±� �ȿ� �ٿ��ֱ��ؼ� dependencies �ȿ� dependency���� �־��ָ� ��

//������ �������� ����� ��ü(bean) ����ϱ�/�������� ����
//������ �����̳� ��ü ����, ���
public class Test {
	public static void main(String[] args) {
		ApplicationContext
		context = new GenericXmlApplicationContext("applicationContext.xml");
		System.out.println("�����̳� ���� �Ϸ�");
		//�����̳ʷκ��� ���� ����� ��ü�� �޾ƿ�
//		Worker worker = (worker) context.getBean("worker"); //object�ϱ� ����ȯ�ؼ� ��������, ��� ���ϸ� �⺻���� object�� ��
		Worker worker = context.getBean("worker", Worker.class); //�̷��� �����͵� ��
		Computer computer = context.getBean("desktop", Computer.class);
		System.out.println("�ΰ��� ���� �Ϸ�");
		worker.setComputer(computer);
		worker.doWork();
		//������ �����̳ʴ�, �� ��ü����, ���� �����?
		//1. �����̳ʰ� ������� ��(23�� ����), ����
		//2. getBean�� �޶��� ��(26, 27������)
		
		//factory-method�� ����. �̴� Worker.java�� �ּ�����
		
		Worker worker2 = context.getBean("worker", Worker.class);
		//worker��ü�� �ϳ� �� ���������? �ƴϴ�. �� ���������. �⺻���� ��å�� singleton�̴�.
		//��, �ϳ� ������ �� ������. �׷��� �Ʒ��� ���� true�� ��
		//lazy-init="true"�� applicationContext id �ڿ� �־��ָ� ���ſ��� ó������ ���ϰ�
		//�ʿ��� �� ȣ����. �̷� ���� �����̳� ���� �� �����ڸ� �θ�
		System.out.println(worker == worker2);
		//applicationContext���� scope�� �⺻�� singleton������
		//scope="prototype"���� �дٸ�, �θ� �� ���� ���� ����� false�� ����
	}
}
