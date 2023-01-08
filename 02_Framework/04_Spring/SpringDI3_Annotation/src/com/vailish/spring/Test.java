package com.vailish.spring;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

public class Test {
	public static void main(String[] args) {
		ApplicationContext
		context = new GenericXmlApplicationContext("applicationContext.xml");
		System.out.println("컨테이너 빌드 완료");
//		Computer computer = context.getBean("desktop", Computer.class);
//		System.out.println(computer.getInfo());
		Worker worker = context.getBean("worker", Worker.class);
//		System.out.println(worker);
		worker.doWork();
	}
}
