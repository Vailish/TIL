# 좋은 웹 AP가 가져가야할 것들
- 성능
- 안정(신뢰)성
- 보안

## 성능
- 온전히 작동한다면 빠르면 빠를수록 좋다
- 사용자 http 요청에 대한 응답 시간을 줄여주자
- 기능 요건에 맞춰 적절히 비동기 처리 여부를 정해보자
- 쓰기보다 읽기가 많은 데이터라면 캐싱을 적극 고려해보자
- ex) RabbitMQ, kafka // EHCACHE, redis, MEMCACHED

## 안정성 - 웹 AP 가치 척도
- 아무리 빠르더라도 제품에 하자가 있다면 사용불가
- 일반적으로 속도보다 우선하는 가치
- 빗발치는 요청을 정상적으로 처리할 수 있어야함
- 데이터가 틀어지거나 서비스 불능 등의 사고는 반드시 막아야 함

## 보안
- 빠르면서 안정적이더라도 안전하지 않다면 매우 심각한 문제
- 보안 분야 스펙트럼은 굉장히 넓어 모든 내용을 섭렵하기란 불가능에 가까움
- '웹' 관련 보안에 관심을 기울이는 노력은 필요함
- 사용자 요청부터 서버에 이르기까지 주요 제품 및 동작에 관한 기본 이해가 있어야만 보안의 기초를 열 수 있음

## 뛰어난 역량의 웹 서버 개발자란?
- 최신 웹 프레임워크 사용 경험만으로 알 수 없음
- 성능, 안정성, 보안과 같은 핵심 가치에 대한 이해도가 높음
- 최신 제품이 위의 핵심 가치를 추구하는데 유리한 면은 많음

## 싱글게임
- 개발자는 language를 사용해 궁극적으로 ''에 저장되는 값을 제어해가며 원하는 기능을 만들어 나간다

### 치트엔진
- 프로세스에서 사용하고 있는 메모리에 담긴 값을 쉽게 수정 가능

## 온라인 게임 서버
- 싱글 게임과 달리 유저로부터 생성되는 데이터는 서버를 통해 관리됨
- 여러 유저들의 정보가 공정하게 관리되어야 함
- 클라이언트 의심은 중요하며, 필요하다

## '너'를 의심
- 사용자 인증 & 인가
- 서버 중심의 견고한 로직 처리
- 사용자 요청의 유효성 검증
- Sql injection, XSS방어

## HTTP
- Hyper Text Transfer Protocol
- Stateless
- HTTP 서버는 불특정 다수의 요청을 전제

## 나를 의심
- 적절한 응답 시간
- 데이터 신뢰성
- 트랜잭션 처리 여부
- 리소스 사용 권한 체크
- 주요 데이터 암호화

## 발생한 일 기록
- 효율적인 logging 구축
- 주요 액티비티 로깅
- 익셉션, 에러 로깅