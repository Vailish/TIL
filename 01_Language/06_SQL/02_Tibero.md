# Tibero
## Function
### CONCAT
- 두 개의 문자열을 접합하여 하나의 문자열을 반환하는 함수.
- ||와 동일
- 두 파라미터 중 하나가 NULL이라도 NULL을 반환하지는 않음
- 예제
```SQL
SELECT CONCAT('ABC', 'DEF') FROM DUAL;
CONCAT('ABC', 'DEF')

-- ABCDEF
```
- [공식문서 - TMAX TechNet](https://technet.tmaxsoft.com/upload/download/online/tibero/pver-20150504-000001/sql-reference/ch_SQL_functions.html#d5e9364)