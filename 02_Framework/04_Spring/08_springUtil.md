# SpringUtil
## countOccurrencesOf
### 개념
- public static int countOccurrencesOf(String str, String sub)
    - str - string to search in / sub - string to search for
- org.springframework.util.StringUtils.countOccurrencesOf
- 주어진 문자열에서 해당 문자열이 얼마나 나오는지 확인하는 메서드

### 예시
```java
@Test
@DisplayName("countOccurrencesOf 테스트")
void countOccurrencesOf() throws Exception{
    String str = "Hello, How are you? Fine Thank you h";
    assertThat(StringUtils.countOccurrencesOf(str, "H")).isEqualTo(2);
    assertThat(StringUtils.countOccurrencesOf(str, ",")).isEqualTo(1);
    assertThat(StringUtils.countOccurrencesOf(str, "y")).isEqualTo(2);
}
```
### 참고
- [Spring docs](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/util/StringUtils.html)
- [블로그 - [Spring Framework] StringUtils](https://blog.seongseob.dev/37)