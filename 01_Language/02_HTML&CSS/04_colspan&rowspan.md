# 태그속성 colspan & rowspan
### `colspan` & `rowspan`
#### colspan
- 셀을 확장(행)하여 하나의 셀처럼 사용할 수 있음
- `<td>`의 `scope` 사용시에도 `colspan`을 통해 사용할 수 있음
![colspan](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fci4etJ%2Fbtq5Ff6henJ%2FKW5OR29UIbZmBDPAjSSlD1%2Fimg.png)
```html
<table>
    <tr>
        <th>밥류</th>
        <th>면류</th>
        <th>분식류</th>
    </tr>
    <tr>
        <td>김밥</td>
        <td>라면</td>
        <td>떡볶이</td>
    </tr>
    <tr>
        <td>주먹밥</td>
        <td colspan="2">라볶이</td>
    </tr>
</table>
```
```html
<table style="border: 1px solid; width: 500px;"> 
    <caption>테이블 예시</caption> 
    <colgroup> 
    	<col style="width: 15%;"/> 
        <col style="width: 35%;"/> 
        <col style="width: 15%;"/> 
        <col style="width: 35%;"/> 
    </colgroup> 
    <tbody> 
    	<tr> 
            <th>컬럼1</th> 
            <td>이것은 데이터1</td> 
            <th>컬럼2</th> 
            <td>이것은 데이터2</td> 
        </tr> 
        <tr> 
            <th>컬럼3</th> 
            <td colspan="3">colspan 3</td> 
        </tr> 
        <tr> 
            <th>컬럼4</th> 
            <td>이것은 데이터3</td> 
            <th>컬럼5</th> 
            <td>이것은 데이터4</td> 
        </tr> 
    </tbody> 
</table>
```

#### rowspan
- 셀을 확장(열)하여 하나의 셀처럼 사용할 수 있음
![rowspan](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbp6CFe%2Fbtq5yC81zbz%2FKbdKCCIpcq7zO5f21PORwk%2Fimg.png)
```html
<table style="border: 1px solid; width: 500px;"> 
    <colgroup> 
    	<col style="width: 5%;"/> 
        <col style="width: 25%;"/> 
        <col style="width: 25%;"/> 
        <col style="width: 25%;"/> 
        <col style="width: 20%;"/> 
    </colgroup> 
    <thead>
    	<tr> 
            <th>no</th> 
            <th>컬럼1</th> 
            <th>컬럼2</th> 
            <th>컬럼3</th> 
            <th>비고</th> 
        </tr> 
    </thead> 
    <tbody> 
    	<tr> 
            <td style="text-align: center;">1</td> 
            <td style="text-align: center;">데이터1</td> 
            <td rowspan="2" style="text-align: center;">rowspan 2</td> 
            <td rowspan="3" style="text-align: center;">데이터3</td> 
            <td style="text-align: center;">메모다.</td> 
        </tr> 
        <tr> 
            <td style="text-align: center;">2</td> 
            <td style="text-align: center;">데이터1</td> 
            <td style="text-align: center;">데이터2</td> 
       <!-- <td style="text-align: center;">데이터3</td> --> 
       <!-- <td style="text-align: center;">메모임.</td> --> 
        </tr> 
        <tr> 
            <td style="text-align: center;">2</td> 
            <td style="text-align: center;">데이터1</td> 
            <td style="text-align: center;">데이터2</td> 
       <!-- <td style="text-align: center;">데이터3</td> --> 
            <td style="text-align: center;">메모임.</td> 
        </tr> 
    </tbody> 
</table>
```


#### 참고
- [블로그 - `[HTML] 테이블(table)의  colspan과 rowspan 사용법과 예시`](https://develop-sense.tistory.com/entry/HTML-%ED%85%8C%EC%9D%B4%EB%B8%94table%EC%9D%98-colspan%EA%B3%BC-rowspan-%EC%82%AC%EC%9A%A9%EB%B2%95%EA%B3%BC-%EC%98%88%EC%8B%9C)