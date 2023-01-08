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
		System.out.println(this.computer.getInfo() + " 로 일합니다.");
	}
	public void setHong(int value) {
		
	}
}
