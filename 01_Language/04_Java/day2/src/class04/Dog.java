package class04;

class Dog {
	String name;
	int age;
	
	Dog() {
//		this.age = 10;
		this("해피");  // 오버로딩할때는 무조건 제일 위에
		this.age = 10;
	}
	
	Dog(String n, int a) {
		name = n;
		age = a;
	}
	
	Dog(int age) {
		this.age = age;
	}
	
	Dog(String name) {
		this.name = name;
	}
	
	void info() {
		System.out.println(this.name);
	}
}
