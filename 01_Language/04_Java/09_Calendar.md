# Calendar
## 개요
- 달력을 다루는 라이브러리
- 사용시 java.util.Calendar를 import 하면됨

## 예시
```java
import java.util.Calendar;

Calendar cal=Calendar.getInstance();	//getInstance()로 객체 생성
    	System.out.println("현재 날짜:"+cal.get(Calendar.YEAR)+"-"+(cal.get(Calendar.MONTH)+1)+"-"+cal.get(Calendar.DAY_OF_MONTH));
    	System.out.println("일주일 중 오늘은 "+cal.get(Calendar.DAY_OF_WEEK)+"번째 요일 (1은 일요일)");
    	System.out.println("일년 중 오늘은 "+cal.get(Calendar.DAY_OF_YEAR)+"번째 날");
    	System.out.println("현재 시간 "+cal.get(Calendar.HOUR_OF_DAY)+":"+cal.get(Calendar.MINUTE)+":"+cal.get(Calendar.SECOND)+":"+cal.get(Calendar.MILLISECOND));
    	System.out.println("현재 시간 "+cal.get(Calendar.AM_PM)+":"+cal.get(Calendar.MINUTE)+":"+cal.get(Calendar.SECOND));
    	System.out.println("이번 주는 일년 중 "+cal.get(Calendar.WEEK_OF_YEAR)+"번째 주");
```

## 참고
- [블로그 - [자바] CALENDAR 클래스의 기본 설명과 여러 예제 모음](https://reakwon.tistory.com/190)

# SimpleDateFormat
## 개요
- 날짜 정보를 간단하게 변환해주는 라이브러리
- 사용시 java.text.SimpleDateFormat를 import 하면 됨

## 예시
```java
String str = simpleDateFormat.format(calendar.getTime()); // 20240214
```



