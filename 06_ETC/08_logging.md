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

# PDD 프로젝트(2022.12.30)에 적용 결과
![스크린샷_20221230_064910](https://user-images.githubusercontent.com/109258380/210057350-8c542ddd-4ee6-4eab-8a6b-736f19a8abaf.png)

![스크린샷_20221230_064926](https://user-images.githubusercontent.com/109258380/210057416-1478da98-4bb8-48a2-9ece-ec1fb5fada4e.png)

![스크린샷_20221230_064935](https://user-images.githubusercontent.com/109258380/210057466-9434aea2-b5a8-48c7-8bcf-841b99bdba4f.png)

![스크린샷_20221230_065106](https://user-images.githubusercontent.com/109258380/210057547-a708a5e9-5055-436a-99a6-997eaecff56b.png)

## 참고 사이트
https://locust.io/
https://wookkl.tistory.com/67