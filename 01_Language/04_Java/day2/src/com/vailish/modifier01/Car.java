package com.vailish.modifier01;

public class Car {
	String color;
	
	private int speed; // 속도는 최소 0, 최대 250까지, private가 붙으면 외부에서 c.speed = 300 이런식으로 못건듦

	public void setSpeed(int speed) {  // 변수를 메서드로 넣으므로써 좀 더 신뢰가게 만들 수 있음
		//int speed?
		if(speed <= 250 && speed >=0 )
			this.speed = speed;
		else
			System.out.println("이상한 속도는 넣지 마세요~");
	}
	public int getSpeed() {
		return this.speed;
	}
}
