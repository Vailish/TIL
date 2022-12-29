package com.vailish.inheritance02;

public class Student extends Person { // final 떄문에 상속 받을 수 없음
	String major;
	
	public Student() {  // 인자안에 아무것도 없으면 컴파일러가 알아서 super()를 넣음
//		super();// super()는 부모의 기본생성자, 만약에 기본이 없으면 안됨, 다른 생성자 양식에 맞추면 그녀석을 호출함
		System.out.println("나는 Student의 기본 생성자야."); 
	}
	
	public void study() {
		super.eat();  
		System.out.println("공부를 한다.");
	}
	
	public void eat() { // 메서드 오버라이딩
		System.out.println("지식을 먹는다.");
	}
	
	@Override
	public String toString() {
		return major + "전공입니다.";
	}
	
	public boolean equals(Object obj) {
		return super.equals(obj);
	}
}
