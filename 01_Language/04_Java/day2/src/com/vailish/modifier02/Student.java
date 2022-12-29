package com.vailish.modifier02;

public class Student {
	private String name;
	private int age;
	private String major;
	
	public Student() {
	}
	
	public Student(String name, int age, String major) {
		this.name = name;
		this.age = age;
		this.major = major;
	}
	
	//getter & setter 만들기
	
	public String getName() {
		return this.name;
	}
	
	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public String getMajor() {
		return major;
	}

	public void setMajor(String major) {
		this.major = major;
	}
	
}
