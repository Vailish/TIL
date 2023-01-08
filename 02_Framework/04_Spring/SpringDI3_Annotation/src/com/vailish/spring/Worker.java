package com.vailish.spring;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

//클래스 첫글자를 소문자로 바꾼 이름이 bean의 이름이 됨!
@Component
public class Worker {
	//내부구현... reflection
	//필드 인젝션의 문제점 : 순환참조에대한 우려가 있기 때문
	@Autowired //                                          1. 필드 인젝션
	private Computer computer; //느슨한 결합 상태
//	@Autowired //(Spring 권장, constructor injection)
//	public Worker(Computer computer) {
////		computer = new Desktop(); //                   2. constructor 인젝션
//		this.computer = computer;
////		System.out.println("Worker의 생성자가 불렸습니다");
//	}
	//자동으로 타입이 일치하는 bean을 찾아다가 여기에 넣어줌(대부분의 상황)
	//두 개 이상이면 에러가 남
	//하지만 여러개일지라도 하나의 빈이 자신과 이름이 같다면 그녀석을 의존설정함
//	@Autowired
//	@Qualifier("desktop") //이렇게 이름을 등록 해도됨
//	public void setComputer(Computer computer) { //        3. property 인젝션
//		this.computer = computer;
//	}

	public void doWork() {
		System.out.println(this.computer.getInfo() + " 로 일합니다." + this.age);
	}
	private int age;
	public void setHong(int value) {//applicationContext에서 상수연결 value, 객체연결 ref 사용
		this.age = value;		
	}
	//자바코드를 건드리지 않고 세팅(applicationContext를 이용해서 결과값을 수정할 수 있다.
	//ex) worker가 데스크탑으로 일할지 노트북으로 일할지 등등 결정이 가능함
}
