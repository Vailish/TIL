# Java 기본 문법
- Java 기본
- 변수와 자료형
- 연산자
- 제어문(조건문 & 반복문)
- 배열
- 다차원 배열

# 운영체제와 프로그램이란?
- 프로그램(Program) : 컴퓨터에서 실행될 때 특정 작업(specific task)을 수행하는 일련의 명령어들의 모음(집합)
- 운영체제(Operating System, OS) : 시스템 하드웨어를 관리할 뿐 아니라 응용 소프트웨어를 실행하기 위하여 하드웨어 추상화 플랫폼과 공통 시스템 서비스를 제공하는 시스템 소프트웨어
  - 사용자와 상호작용

# 컴퓨터의 자료표현
- 비트 (Bit, Binary digit) : 컴퓨터가 `값`을 저장할 수 있는 최소 단위
- 바이트 (Byte) : 컴퓨터가 정보를 처리하기 위한 최소 단위
- 2진수 (Binary)
- 용량단위
  - SI : 10^3 기준(1000) K, M, G, T
  - IEC : 2^10 기준(1024) Ki, Mi, Gi, Ti
    - ex) 00001001(2) -> 9
    - ex) 10001001(2) -> -119 (2의 보수법)
  - 하드 샀을 때 500GB가 475GB로 보이는 이유 SI가 아닌 IEC기준으로 판매하기 때문, 이걸 SI로 보여주니까 줄어든 것 처럼 느끼는 것

# 자바 가상 머신(JVM, Java virtual machine)이란?
- 자바 바이트코드를 실행할 수 있는 주체
- 자바 바이트코드는 플랫폼에 독립적이며 모든 JVM은 자바 가상 머신 규격에 정의된대로 자바 바이트코드를 실행
- Java 원시 프로그램(HelloProgram`.java`)
- -> 컴파일
- -> 자바 바이트 코드(HelloProgram`.class`)
- -> JVM(Mac), JVM(Linux), JVM(Windows)
- JRE(Java Runtime Environment) : 실행시 필요한 것
- JDK(Java Development Kit) : JRE + 개발필요한 것, ex) Zulu-8

# Hello Vailish
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