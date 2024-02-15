# Oracle

## 계층형 쿼리
- 한테이블에 레코드들이 계층관계(상위,하위)를 이루며 존재할 때, 이 관계에 따라 레코드를 계층관계(상위,하위) 한 구조로 데이터를 가져올 때 사용되는 SQL문을 의미한다.
- 계층을 나타내는 쿼리
- 한 컬럼에 어느 레코드의 계층인지 표현함으로써 깊이를 나타냄
- 명령어
    - START WITH로 시작점, CONNECT BY로 자식데이터 설정 가능
    - LEVEL 명령어를 통해 깊이를 SELECT 할 수 있음
    - ORDER SIBLINGS BY 로 정렬가능 / 계층구조 유지하면서 동일 상위계층 하위계층 끼리 정렬
예시 - [블로그 - [ Oracle SQL ] 계층형쿼리 (Hierarchy Query)](https://dev-cini.tistory.com/47)
![계층형쿼리](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FO6zOs%2FbtrDZvh4x0D%2FFbkyQQ712o3H9kv0I5azK1%2Fimg.png)
```sql
CREATE TABLE TB_DEPT
( 
   DEPT_CD     VARCHAR2(8) NOT NULL PRIMARY KEY,
   PAR_DEPT_CD VARCHAR2(8),
   DEPT_NM     VARCHAR2(50)
);

INSERT INTO TB_DEPT(DEPT_CD,PAR_DEPT_CD,DEPT_NM)VALUES('DE_001',NULL,'회사');
INSERT INTO TB_DEPT(DEPT_CD,PAR_DEPT_CD,DEPT_NM)VALUES('DE_002','DE_001','개발부문');
INSERT INTO TB_DEPT(DEPT_CD,PAR_DEPT_CD,DEPT_NM)VALUES('DE_003','DE_001','영업부문');
INSERT INTO TB_DEPT(DEPT_CD,PAR_DEPT_CD,DEPT_NM)VALUES('DE_004','DE_002','개발부');
INSERT INTO TB_DEPT(DEPT_CD,PAR_DEPT_CD,DEPT_NM)VALUES('DE_005','DE_002','부설연구소');
INSERT INTO TB_DEPT(DEPT_CD,PAR_DEPT_CD,DEPT_NM)VALUES('DE_006','DE_003','해외영업부');
INSERT INTO TB_DEPT(DEPT_CD,PAR_DEPT_CD,DEPT_NM)VALUES('DE_007','DE_003','국내영업부');
INSERT INTO TB_DEPT(DEPT_CD,PAR_DEPT_CD,DEPT_NM)VALUES('DE_008','DE_003','영업기획팀');

SELECT 
    LEVEL LEV,
    DEPT_CD,
    DEPT_NM,
    PAR_DEPT_CD
FROM TB_DEPT
START WITH PAR_DEPT_CD IS NULL -- 시작 위치를 정함
CONNECT BY PAR_DEPT_CD = PRIOR DEPT_CD -- 자식데이터를 지정
ORDER SIBLINGS BY DEPT_CD;
```

- 계층형 쿼리 사용의 이점:
    - 계층 구조 표현: 계층형 쿼리는 계층 구조를 쉽게 표현할 수 있습니다. 조직도, 부서 계층, 카테고리 구조와 같은 계층적인 데이터를 쿼리로 나타내기 용이합니다.
    - 재귀적인 쿼리 단순화: 계층형 쿼리는 재귀적인 구조를 단순하게 처리할 수 있습니다. 재귀 쿼리를 사용하지 않고 계층적인 데이터를 조회하려면 반복적인 쿼리나 프로그래밍 로직을 작성해야 할 수 있습니다.
    - 트리 탐색: 계층형 쿼리를 사용하면 트리 구조를 효과적으로 탐색할 수 있습니다. 각 레벨에 따라 데이터를 선택하고 필터링하는 데 유용합니다.
- 계층형 쿼리 사용의 단점:
    - 성능 문제: 대용량 데이터셋에서 계층형 쿼리를 사용할 경우 성능 문제가 발생할 수 있습니다. 계층적인 구조를 재귀적으로 조회하면서 성능에 영향을 미칠 수 있습니다.
    - 가독성 난이도: 복잡한 계층구조에서는 쿼리의 가독성이 낮아질 수 있습니다. 특히 복잡한 조건이나 연산이 있는 경우 쿼리를 이해하고 유지보수하기 어려울 수 있습니다.
    - 유연성 제한: 일부 데이터베이스에서는 계층형 쿼리를 사용하는 것이 제한될 수 있습니다. 특정 데이터베이스 시스템에 따라 구문이나 지원하는 함수의 차이가 있을 수 있습니다.
- 관리 어려움: 계층 구조가 변경되거나 데이터의 삽입/삭제가 빈번하게 일어날 경우, 관리 및 유지보수가 어려워질 수 있습니다.
- 계층형 쿼리를 사용할지 여부는 주어진 상황과 요구사항에 따라 다르며, 적절한 인덱스 및 성능 튜닝을 고려하여 사용하는 것이 좋습니다.
