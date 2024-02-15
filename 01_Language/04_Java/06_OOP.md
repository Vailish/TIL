# OOP(객체지향 프로그래밍)
- 객체지향 프로그래밍
- 클래스
- JVM 메모리구조
- 생성자
- 접근제한자
- 상속

# 객체지향 프로그래밍
## 객체지향 프로그래밍
- OOP, Object Oriented Programing
- 객체 : 사물과 같이 유형적인 것과 개념이나 논리와 같은 무형적인 것들
- 지향 : 작정하거나 지정한 방향으로 나아감
- 객체 모델링 : 현실세계의 객체를 SW 객체로 설계하는 것
- ex) 사람
  - 속성 : 이름, 나이, 키, 몸무게, ...
  - 행동(기능) : 밥을 먹는다, 숨을 쉰다, ...

## 객체지향 프로그래밍 특징(`A PIE`)
- `A`bstraction (추상화)
- `P`olymorphism (다형성)
- `I`nheritance (상속)
- `E`ncapsulation (캡슐화)

# 클래스
- 관련 있는 변수와 함수를 묶어서 만든 사용자정의 <자료형>
- 모든 객체들의 생산처
- 클래스 == 객체를 생성하는 틀, `설계도`
- 프로그래밍이 쓰이는 목적을 생각하여 어떤 객체를 만들어야 하는지 결정
  - 윗줄과 아랫줄 합쳐서 `객체 모델링`
- 각 객체들이 어떤 특징(`속성`과 `동작`)을 가지고 있을지 결정
- 클래스를 통해 생성된 객체를 인스턴스라고 함
- 객체들 사이에서 메시지를 주고 받도록 만들어 줌
- 배열처럼 이름이랑 주소만 stack에 가지고 있고 정보는 heap에 담음
- 클래스 메모리(메소드 메모리)에 클래스 설계도를 가져다 씀

```java
public class Person {
    String name;
    int age;
    String hobby;

    public void info() {
        System.out.println("나의 이름은 " + name + "입니다.");
        System.out.println("나이는 "+age+"세, 취미는 "+hobby+"입니다.");
    }
}
```
## 클래스 구성
- 속성 (Atrribute) : 필드
- 동작 (Behavior) : 메소드
- 생성자 (Constructor) : 인스턴스를 생성할 때 호출 메서드
- inner class : 클래스 안에 클래스

## 클래스 선언
```
[접근제한자] [활용제한자] class 클래스명 {
    속성 정의 (필드)
    기능 정의 (메소드)
    생성자
}
```

# 변수
- 클래스 변수(class variable)
  - 클래스 영역 선언(static 키워드) ex) static int person count;
  - 생성시기 : 클래스가 메모리에 올라갔을 때
  - 모든 인스턴스가 공유함
  - 소멸 : 프로그램 종료시
- 인스턴스 변수(Instance variable)
  - 클래스 영역 선언
  - 생성시기 : 인스턴스가 생성되었을 때 (new)
  - 인스턴스 별로 생성됨
  - 소멸 -> GC
- 지역 변수(local variable)
  - 클래스 영역 이외 (메서드, 생성자 등)
  - 생성시기 : 선언되었을 때
  - 사용하기전에 초기화 필수!
  - 외부 접근 불가
  - 소멸 : 중괄호 벗어나면 소멸

# 메소드 (Method)
- 객체가 할 수 있는 행동을 정의
- 어떤 작업을 수행하는 명령문의 집합에 이름을 붙여 놓은 것
- 메소드의 이름은 소문자로 시작하는 것이 관례
```
[접근제한자] [활용제한자] 반환값 메소드이름([매개변수들]) {
    행위기술
}
ex) public static void main(String [] args){}
```
- 접근제한자 : public / protected / default / private
- 활용제한자 : static / final / abstract / synchronized
```java
public class Person {
    public void info() {
        // 메소드 내용 정의
    }
    
    public static void hello() {
        // 메소드 내용 정의
    }
}
```
- 메소드 선언 : 선언시 {}안에 메소드가 해야 할 일을 정의
- 메소드 호출
  - 호출한 메소드가 선언되어 있는 클래스를 접근
  - 클래스 객체.메소드 이름으로 호출
    - ex) Person p = new Person(); p.info();
  - static이 메소드에 선언되어 있을 때는 클래스이름.메소드 이름으로 호출
    - ex) Person.hello();

```java
public void study(int time) {
    // int time = ?
    // 파라미터는 해당 위치에 선언한 지역변수
    System.out.println(time+"시간 공부.");
}
Person p = new Person();
p.study(10);
```
- 매개변수(Parameter) : 메소드에서 사용하는 것
- 인자(Argument) : 호출하는 쪽에서 전달하는 곳
- 매개변수 생략 가능
- 파라미터 전달 시 묵시적 형 변환
  - ex) 위의 예시에서는 p.study((byte) 10); p.study((short) 10); p.study(10); 이렇게는 가능하지만
  - 더 큰 녀석인 p.study(10L); p.study(10.0f); p.study(10.0); 불가, p.study(10, 10)도 불가
```java
public int getAge() {
    return age;
}

Person p = new Person();
p.name = "Yang";
p.age = 45;
p.hobby = "유튜브";

int age = p.getAge();
```
- 리턴 타입은 메소드를 선언할 때 지정, 없다면 void (return문 생략 가능)
- 리턴 타입을 작성했다면 반드시 해당 타입의 값을 리턴
- 리턴 타입은 하나만 적용가능

```java
System.out.println()
```
- 메소드 오버로딩(Overloading)
  - 이름이 같고 매개변수가 다른 메소드를 여러 개 정의하는 것
  - 중복 코드에 대한 효율적 관리 가능
  - 파라미터의 개수 또는 순서, 타입이 달라야 할 것 (파라미터 이름만 다른것은 X)
  - 리턴 타입이 다른 것 의미X

## 클래스와 객체
- 클래스 : 관련 있는 변수와 함수를 묶어 만든 사용자 정의 자료형
- 객체 : 하나의 역할을 수행하는 '메소드와 변수(데이터)'의 묶음
- 객체지향 프로그래밍 : 프로그램을 단순히 데이터와 처리 방법으로 나누는 것이 아니라, 프로그램을 수많은 '객체(object)'라는 기본 단위로 나누고 이들의 상호작용으로 서술하는 방식

# JVM 메모리구조
## JVM 메모리 구조
- Java언어는 메모리 관리를 개발자가 하지 않음.
- GC(Garbage Collection)가 메모리 관리
  - Heap 영역(class 영역 포함)에 생성된 메모리 관리 담당
  - 더 이상 사용되지 않는 객체들을 점검하여 제거
  - 자동적 실행 / CPU가 한가하거나 메모리 부족일 때
  - JVM에 의해서 실행
  - System.gc()를 통해 호출(시스템에 영향 주면서 하지말자)
  - [관련 링크](https:/d2.naver.com/helloworld/1329)
![image](https://user-images.githubusercontent.com/109258380/209677501-2b57666f-9d41-431e-b3ec-fe83b4848400.png)

## 객체 생성과 메모리 할당

# Static 특징
## 로딩 시점
  - static : 클래스 로딩 시
  - non-static : 객체 생성시

## 메모리상의 차이
  - static : 클래스당 하나의 메모리 공간만 할당
  - non-static : 인스턴스 당 메모리 별도 할당
## 문법적 특징
- static : 클래스 이름으로 접근
- non-static : 객체 생성 후 접근
```java
Public class Person {
    static int pCount;

    String name;
    int age;
    String hobby;
}

Public class PersonTest {
    public static void main(String[] args) {
        Person p = new Person();
        p.name = "Kim";

        Person.pCount++;

        p.pCount++; //오류는 나지 않고 경고, 위의 방식 권장
    }
}
```
## static 영역에서 non-static 영역을 직접 접근이 불가능
```java
Public class Main {

    String str = "문장";

    public static void main(String[] args) {
        System.out.println(str); // 불가
    }
}
```

## non-static 영역에서는 static 영역에 대한 접근이 가능
```java
public class Main {
    
    static String str = "문장";

    public void print() {
        System.out.println(str);  // 가능
    }
}
```

# 생성자
## 인스턴스가 생성될 때 최초 한 번 수행되는 함수
- new 키워드와 함께 호출
- 클래스를 생성할 때 반드시 하나의 생성자 호출
- 성공적으로 실행되면 힙 영역에 객체 생성 후 객체의 번지가 리턴
- 필드의 초기화, 객체 생성 시 실행되어야 할 작업 작성
- PascalCase로 작성하는 것이 관례

## 생성자 특징
- 클래스 명과 이름이 동일(대,소문자)
- 반환타입이 없음(void 작성 x)
```java
Public class Dog {
    public Dog() {
        System.out.println("기본 생성자!");
        System.out.println("클래스 이름과 동일하고 반환 타입 X");
    }
}
```
- 기본(디폴트) 생성자
  - 클래스 내에 생성자가 하나도 정의되어 있지 않을 경우 JVM이 자동으로 제공하는 생성자
  - 형태 : 매개변수가 없는 형태, 클래스 명() {}
  - ex) Dog d = new Dog();
- 파라미터가 있는 생성자
  - 생성자의 목적이 필드 초기화
  - 생성자 호출 시 값을 넘겨주어야 함
  - 해당 생성자를 작성하면 JVM에서 기본 생성자를 추가하지 않음
```java
class Dog {
    String name;
    int age;
}

class Main {
    public static void main(String [] a) {
        Dog d1 = new Dog();
        d1.name = "쫑";
        d1.age = 3;
    }
}

// 만약 아래와 같이 바꼇다면
class Dog(String n, int a) { // 생성자
    name = n;
    age = a;
}
// Dog d1 = new Dog(); 못 씀, 생성자 정의한 순간 기본값으로 못 만들기때문에 사용불가
// Dog d2 = new Dog("메리", 4); 와 같이 써야함
```
- 생성자 오버로딩을 지원
  - 클래스 내에 메소드 이름이 같고 매개변수의 타입 또는 개수가 다른 것
  - 이름만 바꾸는건 오버로딩아님! ex) int age -> ages 이런거
```java
class Dog {
    Dog() { }
    Dog(String name) { }
    Dog(int age) { }
    Dog(String name, int age) { }
}

class Main {
    public static void main(String [] a) {
        Dog d = new Dog();
        Dog d2 = new Dog("쫑");
        Dog d3 = new Dog(3);
        Dog d4 = new DOg('메리', 4);
    }
}
```
- this
  - 참조 변수로써 객체 자신을 가리킴(객체의 주소)
  - this를 이용하여 자신의 멤버 접근 가능
  - 지역변수와 필드의 이름이 동일할 경우 필드임을 식별할 수 있게 함
  - 객체에 대한 참조이므로 static 영역에서 this 사용 불가
- this의 활용
  - `this.멤버변수`
  - this([인자값..]) : 생성자 호출
  - this 생성자 호출 시 제한사항
    - 생성자 내에서만 호출이 가능함
    - 생성자 내에서 첫번째 구문에 위치해야 함
```java
class Dog {
    String name;
    int age;
    void info ( ) {
        System.out.print(this.name);
        System.out.println(this.age);
    }
}
```
```java
class Dog {
    String name;
    int age;
    Dog ( ) {
        this("쫑");
    }
    Dog ( String name) { //이 경우에 name에 "쫑이 들어간것과 같음"
        
    }
}
```

# 패키지(package)
- PC의 많은 파일을 관리하기 위해서 `폴더`를 이용
- 프로그램의 많은 클래스를 관리하기 위해서 `패키지`를 이용
- 패키지는 클래스와 관련 있는 인터페이스들을 모아두기 위한 이름 공간
- 패키지의 구분은 .(dot) 연산자를 이용
- 패키지의 이름은 시중에 나와 있는 패키지들과 구분되게 지어야 함
- 일반적으로 소속이나 회사의 도메인을 사용
  - ex) com.Vailsh.project_이름.moduel_이름

# 임포트(import)
- 다른 패키지에 있는 클래스를 사용하기 위해서는 import 과정이 필요함
- PersonService.java에서 Person 클래스를 사용하기 위해서는 import 해야 함
- import를 선언 할 때는 import 키워드 뒤에 package 이름과 클래스 이름을 모두 입력하거나 해당 패키지의 모든 클래스를 포함할 때는 '*'를 사용하기도 함

```java
// import package_name.class_name;
// import package_name.*; // 전체

package com.vailish.project.service;
import com.vailish.project.dto.Person;
public class PersonService {
  Person p;
}
```
# 캡슐화(Encapsulation)
- 객체의 속성(data fields)과 행위(메서드, methods)를 하나로 묶고
- 실제 구현 내용 일부를 외부에 감추어 은닉
![image](https://user-images.githubusercontent.com/109258380/209847226-d0fbd31a-8e95-494b-84c2-0db97c274387.png)

# 접근제한자(access modifier)
- 클래스, 멤버 변수(필드), 멤버 메서드 등의 선언부에서 `접근 허용 범위`를 지정하는 역할의 키워드
- 접근 제한자의 종류
  - public
  - protected
  - (default)
  - private
- 그 외 제한자
  - static : 클래스 레벨의 요소 설정
  - final : 요소를 더 이상 수정할 수 없게 함
  - abstract : 추상 메서드 및 추상 클래스 작성
  - ...

## 접근 제한자
- public : 모든 위치에서 접근이 가능
- protected : 같은 패키지에서 접근이 가능. 다른 패키지 접근 불가능, 단, 다른 패키지의 클래스와 상속관계가 있을 경우 접근 가능
- (default) : 같은 패키지에서만 접근이 허용, 접근 제한자가 선언이 안 되었을 경우 기본 적용
- private : 자신 클래스에서만 접근이 허용
- 클래스(외부) 사용가능 : public, default
- 내부클래스, 멤버변수(필드), 메소드 사용가능 : 4가지 모두 가능

|수식어|클래스 내부|동일 패키지||(다른 패키지내의) 하위 클래스)||다른 클래스|
|------|---|---||---||---|
|private|o||||
|(default)|o|o|||
|protected|o|o|o||
|public|o|o|o|o|

# 접근자(getter) / 설정자(setter)
- 클래스에서 선언된 변수 중 접근제한에 의해 접근할 수 없는 변수의 경우 다른 클래스에서 접근할 수 없기 때문에, 접근하기 위한 메서드(설정자와 접근자)를 public으로 선언하여 사용
- 우클릭하면 소스에 getter setter 생성이 있음(자동완성)
```java
public class Person {
  private String name;
  private int age;

  public String getName() {
    return name;
  }

  public int setName(String name) {
    this.name = name
  }

  public void setAge(int age) {
    this.age = age;
  }
}
```

# 상속
- 어떤 클래스의 특성을 그대로 갖는 새로운 클래스를 정의한 것
- 상위 클래스, 부모클래스, 자식클래스
1. 확장성, 재 사용성 - 부모의 생성자와 초기화 블록은 상속 x
2. 클래스 선언 시 extends 키워드를 명시
  - 자바는 다중 상속 허용X, `단일 상속` 지원
3. 관계
  - 부모(상위, Super)클래스 : Person
  - 자식(하위, Sub)클래스 : Student
4. 자식 클래스는 부모 클래스의 멤버변수, 메소드를 자신의 것처럼 사용할 수 있음
  - 단, 접근 제한자에 따라 사용 여부가 달라짐
5. Object 클래스는 모든 클래스의 조상 클래스
  - 별도의 extends 선언이 없는 클래스는 extends Object가 생략
6. super 키워드
  - super를 통해 조상 클래스의 생성자 호출
7. 오버라이딩(재정의, overriding) : 이걸 붙임으로써 좀 더 안전한 코드가 됨
  - 상위 클래스에 선언된 메서드를 자식 클래스에서 재정의 하는 것
  - 메서드의 이름, 반환형, 매개변수 (타입, 개수, 순서) 동일해야 함
  - 하위 클래스의 접근제어자 범위가 상위 클래스보다 크거나 같아야함
  - 조상보다 더 큰 예외를 던질 수 없음
  - 메서드 오버로딩(overloading)과 혼동하지 말자!
```
@ : Annotation 컴파일러가 보는 주석
@Override
public void eat() {
  ~~~~
}
```

## Object
- Object 클래스
  - 가장 최상위 클래스로 모든 클래스의 조상
  - Object의 멤버는 모든 클래스의 멤버
![image](https://user-images.githubusercontent.com/109258380/209976574-82aa9a11-53c7-47b3-9c89-08a610a7b140.png)

## equals 메서드
- 두 객체가 같은지를 비교하는 메서드
```java
public boolean equals(Object obj) {
  return (this == obj);  // 등가비교 연산자 ==로 두 객체의 `주소값` 비교
}
```
- 두 개의 레퍼런스 변수가 같은 객체를 가리키고 있나?
![image](https://user-images.githubusercontent.com/109258380/209977596-6fad7506-df4e-408e-96d0-e6cef7fc723e.png)
- 우리가 비교할 것은 정말 객체의 주소인가
  - 두 객체의 내용을 비교할 수 있도록 equals 메서드 재정의
```java
private static void testString() {
  String s1 = new String("Hello");
  String s2 = new String("Hello");
  System.out.println((s1 == s2) + " : " + s1.eqauls(s2));
}

private static void testPhone() {
  Phone p1 = new String("01000000000");
  Phone p2 = new String("01000000000");
  System.out.println((p1 == p2) + " : " + p1.eqauls(p2));
}

class Phone {
  String number = "전화번호";

  public Phone(String number) {
    this.number = number;
  }
}

@Override
public boolean equals(Object obj) {
  if (obj != null && obj instanceof Phone) {
    Phone casted = (Phone) obj;
    return number.equals(casted.number);
  }
  return false;
}
```

## hashCode
- 객체의 해시 코드 : 시스템에서 객체를 구별하기 위해 사용되는 정수값
- HashSet, HashMap 등에서 객체의 동일성을 확인하기 위해 사용
- equals 메서드를 재정의 할 때는 반드시 hashCode도 재정의 할 것
- 미리 작성된 String이나 Number 등에서 재정의 된 hashCode 활용 권장
![image](https://user-images.githubusercontent.com/109258380/209978937-43a95770-8d36-4f63-b9ea-4ec76d60051b.png)

# final
- 해당 선언이 최종상태, 결코 수정 될 수 없음
- final 클래스 : 상속 금지
- final 메소드 : overriding 금지
- final 변수 : 더 이상 값을 바꿀 수 없음 상수화
- ex) MYCOMPUTER의 경우 MY_COMPUTER 이런식으로 쓰는 것이 관례
