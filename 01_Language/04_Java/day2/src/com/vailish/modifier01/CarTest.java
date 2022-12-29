package com.vailish.modifier01;

public class CarTest {
	public static void main(String[] args) {
		//자동차 하나 생성.
		
		Car c = new Car();  // 같은 패키지이기 car class가 default이므로 사용가능
		c.color = "Red";
//		c.speed = 100;
//		
//		c.speed = 300; // 이렇게 작성한 것은 막을수 있나? 없다, 그래서 외부에서 접근 못하게 만들고 싶다
//		System.out.println(c.speed); // private으로 만들었으니 읽지도 못함...
	}
}
