- 중복구현을 막기위한 패턴들...

# Template Method pattern(템플릿 메소드 패턴)
- 공통된 부분을 따로 모아서 클래스로 만든다.
- 바뀌는 부분만 추상클래스로 만들어주고 만든 클래스안에 변경되는 부분에 해당 추상클래스를 집어 넣어 바인딩해준다. 상속받았을 때 해당 부분을 넣어 줌으로써 원하는 데로 설정해준다.
- 수직적인 구조

# Strategey Pattern(전략 패턴)
- 만약에 하위 클래스의 기능이 각각 몇개씩 공통된 부분이 있다면 어떻게 해야할까?
- 이러할 때에는 기능별로 따로 구현해서 상속받을 때 참조하는 방식으로 해결할 수 있다.
- 기능별 구조
- 나눠진 전략을 그때 그때 동적으로 적용

## 제어의 역전
- IoC 제어의 역전
- 의존성은 new(생성자)에서 나옴
- 이 의존성을 한곳에다가 다 몰아 넣을 수 있음.
- 이것이 Spring container이고 이것이 스프링의 본질임
```java
// Emoloyee.java
package 전략패턴0;

public class Employee extends Person{
//	private DoWork work = new DoWork(); //new를 여기가 아닌 test에서 사용하게끔 변경(IoC)
	private DoWork work;
	private EatWellStory wellStory = new EatWellStory();
	public Employee(DoWork work) {
		this.work = work;
	}
	
	@Override
	public void doSomething() {
		// TODO Auto-generated method stub
		work.doSomething();
		wellStory.doSomething();
	}

}


// Test.java
package 전략패턴0;

public class Test {
	public static void main(String[] args) {
		//work에 대한 의존성이 Employee에서 Test로 이관됨.
		//이것이 IoC(제어의 역전)
		DoWork work = new DoWork();
		//Test가 work를 Employee에 넣어줬다
		//이것이 DI(의존성 주입)
		Person p = new Employee(work);
		p.daily();
	}
}

```

## DI(Dependency Injection) : 의존성 주입
- 의존성(Dependency)
- ClassA 객체가 어떤 일을 처리하기 위해서 ClassB의 객체의 도움을 받아야만 일을 처리할 수 있다면 'ClassA는 ClassB에 의존한다.'라고 표현
```java
public class Store {
    private Item obj = new ItemImp(); // 01)
    public void doSomething();
        obj.func();
}
//01) ClassA가 ClassB의 객체를 사용하기 위해서 클래스 내부에서 직접 객체를 생성(의존성 주입)
```