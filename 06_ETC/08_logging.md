# 로깅
- logging : 시스템에서 발생한 사건(event)을 기록하는 것
- log : 로깅의 결과물 - 유지보수에 있어 `블랙박스`와 같은 역할
- why?
  - 문제를 찾기 위해
  - 원인을 찾기 위해
  - 사용자 행동을 분석하기 위해
  - 야근방지를 위해...

## 개발 언어와 프레임워크에 알맞은 로깅 방법을 사용하자
- Spring Boot : Logback, Log4j2
- Python(Django,Flask,...) : Python Logging Module
- Node : Winston, Pino, Bunyan
- FE : 중요 로그는 백엔드로 보내자. 또는 솔루션과 서비스(SaaS)를 적용하자

## 로깅 레벨을 구분하여 사용하자
- FATAL(CRITICAL, SEVERE) > ERROR > WARN > INFO > DEBUG > TRACE
- 개발 환경에 따라 로그 출력을 구분하자
  - 상세한 로그 순 : Local(TRACE) > Dev(DEBUG) > Test(INFO) > Prod(WARN|ERROR)

## 로그 저장
- 로그는 중요한 자원이고, 다른 팀원도 볼 수 있게 끔 파일로 많이 남김
- DB에 저장해도 되지만, DB는 비싼 자원이기 때문에 저장여부 결정 시 한 번 생각을 해봐야 됨