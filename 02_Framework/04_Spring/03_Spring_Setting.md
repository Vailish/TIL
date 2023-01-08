# Spring Setting
- Spring library setting
- Spring setting file 작성
- Spring container build

## Spring 라이브러리 세팅

## Spring setting file 작성

## Spring container 빌드

```xml
<bean class="com.vailish.spring.Desktop" id="desktop"></bean>
```
```java
Desktop desktop = new Desktop();
```
- 여기서  `class="com.vailish.spring.Desktop"`는 new `Desktop();`을 의미
- id 뒤의 `desktop`은 Desktop `desktop`을 의미

## 설정자 주입과 생성자 주입의 차이
- 설정자 주입 : 중간에 의존관계를 자바코드단에서 동적으로 바꿔낄 수 있다는 특성이 있음
- 생성자 주입 : 주입을 하지 않고서는 객체를 생성 할 수 없음, 좀 더 엄격함
- 어떤게 더 좋다라는 것은 없다.