# 변수와 자료형
- 변수
- 자료형
- 변수와 자료형
- 변수
- 자료형
- 형변환

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
- 데이터 형변환
  - 묵시적(암묵적) : Implicit Casting
    - 범위가 넓은 데이터 형에 좁은 데이터 형을 대입하는 것
    - ex) byte b = 100; int i = b;
  - 명시적 : Explicit Casting
    - 범위가 좁은 데이터 형에 넓은 데이터 형을 대입하는 것
    - 형 변환 연산자 사용 - (타입) 값;
    - ex) int i = 100; byte b = i; (X), byte b = (byte)i; (O)