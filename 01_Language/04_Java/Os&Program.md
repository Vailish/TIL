# Java 기본 문법
- Java 기본
- 변수와 자료형
- 연산자
- 제어문(조건문 & 반복문)
- 배열
- 다차원 배열

## 운영체제와 프로그램이란?
- 프로그램(Program) : 컴퓨터에서 실행될 때 특정 작업(specific task)을 수행하는 일련의 명령어들의 모음(집합)
- 운영체제(Operating System, OS) : 시스템 하드웨어를 관리할 뿐 아니라 응용 소프트웨어를 실행하기 위하여 하드웨어 추상화 플랫폼과 공통 시스템 서비스를 제공하는 시스템 소프트웨어
  - 사용자와 상호작용

## 컴퓨터의 자료표현
- 비트 (Bit, Binary digit) : 컴퓨터가 `값`을 저장할 수 있는 최소 단위
- 바이트 (Byte) : 컴퓨터가 정보를 처리하기 위한 최소 단위
- 2진수 (Binary)
- 용량단위
  - SI : 10^3 기준(1000) K, M, G, T
  - IEC : 2^10 기준(1024) Ki, Mi, Gi, Ti
    - ex) 00001001(2) -> 9
    - ex) 10001001(2) -> -119 (2의 보수법)
  - 하드 샀을 때 500GB가 475GB로 보이는 이유 SI가 아닌 IEC기준으로 판매하기 때문, 이걸 SI로 보여주니까 줄어든 것 처럼 느끼는 것

## 자바 가상 머신(JVM, Java virtual machine)이란?
- 자바 바이트코드를 실행할 수 있는 주체
- 자바 바이트코드는 플랫폼에 독립적이며 모든 JVM은 자바 가상 머신 규격에 정의된대로 자바 바이트코드를 실행
- Java 원시 프로그램(HelloProgram`.java`)
- -> 컴파일
- -> 자바 바이트 코드(HelloProgram`.class`)
- -> JVM(Mac), JVM(Linux), JVM(Windows)
- JRE(Java Runtime Environment) : 실행시 필요한 것
- JDK(Java Development Kit) : JRE + 개발필요한 것, ex) Zulu-8

## Hello Vailish
```java
import java.lang.*;    // 생략가능
public class Hello {
    public static void main(String[] args) {
        System.out.println('Hello Vailish!!!');
    }
}
// [Hello.java]로 저장
```
cmd에서 javac Hello.java 하면 바이트코드로 바꿔줌
그 뒤에 java Hello
>>>[Hello Vailish!!!]

이런 것을 해주는 것 : IDE
IDE : 통합 개발환경
ex) eclipse

## main method
- 실행 명령인 java를 실행 시 가장 먼저 호출 되는 부분
- 만약, Application에서 main() 메소드가 없다면 절대로 실행 될 수 없음
- Application의 시작 -> 특정 클래스의 main() 실행
- 형태 (고정된 형태)
```java
public static void main(String[] arges){}
```
# 주석(Comment)
```java
public class Intro02_Comment {
	public static void main(String[] args) {
		// 기호가 등장한 순간부터 끝까지 해당 줄을 주석처리
		// 단축키는 파이썬과 동일하게 ctrl + /
		
		/*
		 	해당 범위를 주석처리 하겠다
		 */
		
		/**
		 * Documentation API 위한 주석
		 */
	}
}

```


## 출력문
- print : 한 줄 출력
- println : 
- printf
  - %d : 정수
  - %f : 실수
  - %c : 문자
  - %s : 문자열

```java
		//print 를 써보자
		System.out.print("Hello Word!! \n");
		// \n : 줄 바꿈, 파이썬과 동일
		
		// println을 써보자
		// sysout + ctrl + space 하면 자동완성해줌
		System.out.println("Hello World!!");
		System.out.println("Hello World!!");
		
		System.out.println("\\"); // 두개를 써야지 \ 가 출력됨
		System.out.println("\"");  // "
		
		System.out.printf("%d \n", 10); //정수 (10진수)
		System.out.printf("%o \n", 10); //정수 (8진수)
		System.out.printf("%X \n", 10); //정수 (16진수)
		System.out.printf("%x \n", 10); //정수 (16진수)
		
		System.out.printf("%4d\n \n", 10); // 4칸을 확보한 뒤 오른쪽부터 차지
		System.out.printf("%-4d\n \n", 10); // 4칸을 확보한 뒤 왼쪽부터 차지
		System.out.printf("%04d\n \n", 10); // 4칸을 확보한 뒤 오른부터 차지(빈칸을 0을 채움)
		
		System.out.printf("%f\n", 10.1); //실수
		System.out.printf("%.2f\n", 10.1); //실수 (소수점 둘째자리까지)
		
		System.out.printf("%s\n", "Vailish");
		System.out.printf("%c\n", 'o');
		
		System.out.printf("안녕하세요. 저는 %s입니다. 제 혈애액형은 %c일껄요?", "Vailish", 'C');
```

# 변수와 자료형
- 정의
  - 데이터를 저장할 메모리의 위치를 나타내는 이름
  - 메모리 상에 데이터를 보관할 수 있는 공간을 확보
  - 적절한 메모리 공간을 확보하기 위해서 변수의 타입 등장
  - '='를 통해서 CPU에게 연산작업을 의뢰
- 메모리 단위
  - 0과 1을 표현하는 bit
  - 8bit = 1byte

## 변수(Variable)
- 대소문자를 구분함
- 공백은 허용안됨
- 숫자로 시작할 수 없음
- '$'와 '_'를 변수 이름에 사용할 수 있음, 이외의 특수문자 불가
- 예약어(ex) println)는 사용 불가
- 합성어의 경우 주로 camelCase를 활용
  - 보통 관례
  - PascalCase : 클래스 이름
  - camelCase : 변수명, 함수
  - snake_case : 상수 => 대문자_대문자 / (python의 경우 많이씀)
  - kebob-case : HTML/CSS 등 속성
- 한글을 이용한 변수 작명가능

## 자료형(DataType)
- 기본 자료형(Primitive Type)과 참조 자료형(Reference Type, 기본 자료형 8가지 외 모든 것)
- 기본 자료형 : 미리 정해진 크기의 Memory Size 표현, 변수 자체에 값 저장
- 실수형의 경우에는 부동소수점 표현 이슈가 있음!
  - 정확한 값이 아니기 때문에 일어나는 문제
![image](https://user-images.githubusercontent.com/109258380/208572871-87a238d5-c3a7-471b-827e-bdd1bd7b0f3a.png)
- cf) String : 참조자료형

## 변수와 자료형
- 선언
  - 자료형 변수명;
  - ex) int age; String name;
- 저장(할당)
  - 변수명 = 저장할 값;
  - 예) age = 30; name = "vailish';
- 초기화
  - 자료형 변수명 = 저장할 값;
  - ex) int age = 30;
- 참조형은 주소를 저장, 기본형은 저장

## 형 변환(Type Casting)
- 자료형의 크기 비교
```
byte < short < int < long < float < double
       char  < int < long < float < double
```
  - short : 음수 가능 / char 음수 불가
  - long이 8byte고 float가 4byte지만 float가 더 큰 이유는 표현하는 커버리지가 더 크기 때문
    - long 2^63 ~ 2^63-1
    - float 10^~~~
    - 단위부터 다름