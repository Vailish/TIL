package com.vailish.spring;

public class Worker {
	private Computer computer; //느슨한 결합 상태
//	public static Worker getinstance() {
//		return new Worker();
//		// 이런식으로 사용하려면 applicationContext에서 id 앞에 factory-method="getInstance"를 사용해도 됨. 자주 안씀
//		
//	}
	public Worker() {
//		computer = new Desktop();
		System.out.println("Worker의 생성자가 불렸습니다");
	}
	public void setComputer(Computer computer) {
		this.computer = computer;
	}
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
