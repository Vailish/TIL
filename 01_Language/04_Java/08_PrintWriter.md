# [파일 입출력](https://wikidocs.net/227)

## PrintWriter
- FileWriter를 사용하더라도 \r\n을 문자열 뒤에 덧붙여야 해 번거롭다. 이런 불편함을 해소하려면 FileWriter 대신 PrintWriter를 사용하면 된다. PrintWriter를 이용하면 \r\n을 덧붙이는 대신 println이라는 메서드를 사용할 수 있다. 다음은 PrintWriter를 이용하여 파일을 작성하는 예제이다.
```java
import java.io.IOException;
import java.io.PrintWriter;

public class Sample {
    public static void main(String[] args) throws IOException {
        PrintWriter pw = new PrintWriter("c:/out.txt");
        for(int i=1; i<11; i++) {
            String data = i+" 번째 줄입니다.";
            pw.println(data);
        }
        pw.close();
    }
}
```
### System.out
```java
for(int i=1; i<11; i++) {
    String data = i+" 번째 줄입니다.";
    System.out.println(data);
}
```
!(printWriter)[https://wikidocs.net/images/page/227/06-02_file1.png]
!(System.out)[https://wikidocs.net/images/page/227/06-02_file2.png]

### 스트림(컴퓨팅)
- 컴퓨터 처리 환경에서 스트림은 시간이 지남에 따라 사용할 수 있게 되는 일련의 데이터 요소
- 일련의 과정 어떤한 일의 흐름, 하드웨어(병렬 컴퓨팅 등) 에서도 사용함