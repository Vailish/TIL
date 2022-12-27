# Sequence
- 자동으로 증가(감소)하는 숫자를 생성시키는 객체
- MySQL 에서는 Auto Increment 속성으로 처리
- Oracle, PostgreSQL 등에서는 Sequence 객체를 통해 관리

```
SELECT LAST_VALUE FROM Sequence 명 : 시퀀스 객체의 현재 값
NEXTVAL(Sequence 명) : 시퀀스 객체의 다음 값
```

# Database Backup 
- [Utility Not Found 오류](https://while1.tistory.com/m/entry/PostgreSQL-file-not-found-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0%ED%95%98%EA%B8%B0)
- 엑세스 거부가 나온다면 관리자 모드로 pgAdmin4를 실행해서 다시해보자!