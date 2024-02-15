# MSA
- Microservice Architecture 

## Monolithic와 MSA

### Monolithic
- 애플리케이션 안에 모든 비즈니스 로직이 다 들어가 있는 구조
- ![MSA vs Monolithic 1](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FnfpnO%2FbtrFvr49iqP%2FARikUA50TCjykjadZwCtnk%2Fimg.png)
- ![MSA vs Monolithic 2](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FKpmMQ%2FbtrFt9qPqPW%2F2qFqpZ3Gik1du8xDvgZkUK%2Fimg.png)

### MSA
- 서비스를 비즈니스 경계에 맞게 세분화 하고, 서비스 간 통신은 네트워크 호출을 통해 진행하여 확장 가능하고 회복적이며 유연한 어플리케이션을 구성하는 것

- ![MSA구조](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdyWgNc%2FbtrFybNLr7G%2FIisQuI7HcOgfweIlD3dw20%2Fimg.png)

## MSA - Microservice Architecture
### 등장배경
- ![MSA 등장배경](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FchMx6b%2FbtrFuonOlVK%2F98jPXGwVVOLturfVYgkWp0%2Fimg.png)
- 기존의 Monolithic 방식은 소프트웨어의 모든 구성요소가 한 프로젝트에 합쳐져있어, 큰 변화에 대한 대응이 어렵고, 새로운 기능 추가 및 업데이트에 어려움이 있었다.
- Monolithic Architecture 는 여러 역할을 하는 시스템이 하나의 소프트웨어로 집합되어 있어, 특정 부분에 문제가 발생 시, 큰 장애로 이어질 수 있다.
- Monolithic Architecture 는 여러 역할을 하는 시스템이 하나의 서버에 함께 올라가있기에 , Scale-out 시 필요없는 자원이 함께 증가된다.
(조회 기능이 90% 이상 사용되고, 사용량이 점점 늘어나고 있다 & 조회만 빈번한 수정이 필요해서 배포가 필요하다
-> 이런 경우 MSA 가 효율적이다.)
- ![MSA Scale-out1](https://velog.velcdn.com/images/dmchoi224/post/42d7ea10-7d6b-43e2-a0b6-0a1d064ccc05/image.png)
- ![MSA Scale-out2](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkX05z%2FbtrFybG08f9%2FwLmbkPnfMGYmcM8JAHRjsk%2Fimg.png)

### MSA 배포
- 민첩하고 손쉬운 배포 및 업데이트를 통해 리스크를 경감시킬 수 있음
![MSA배포](https://velog.velcdn.com/images/dmchoi224/post/460b28fe-cfdd-4789-b69d-c779232f246e/image.png)

### MSA Component
- ![image](https://github.com/Vailish/git-practice/assets/109258380/750d0209-1f1a-44bb-a7d3-52784fc486e1)
    1. Config Management
        - 서비스의 재빌드, 재부팅 없이 설정사항을 반영(Netflix Archaius, Kubernetes Configmap)
    2. Service Discovery
        - MSA기반 서비스 배포 시 서비스 검색 및 등록(Netflix Eureka, Kubernetes Service, Istio)
    3. API Management
        - 클라이언트 접근 요청을 일원화(Netflix Zuul, Kubernetes Ingress)
    4. Centralized Logging
        - 서비스별 로그의 중앙집중화(ELK Stack)
    5. Distributed Tracing
        - 마이크로서비스 간의 호출 추적(Spring cloud Sleuth, Zipkin)
    6. Centralized Monitoring
        - 서버별 메트릭 정보의 중앙집중화(Netflix Spectator, Heapster)
    7. Resilience & Fault Tolerance
        - MSA 구조에서 하나의 실패한 서비스가 체인에 연결된 전체 서비스들에 파급 효과를 발생시키지 않도록 하기 위한 계단식 실패 방지 구조(Netflix Hystrix, Kubernetes Health check)
    8. Auto-Scaling & Self-Healing
        - 자동 스케일링, 복구 자동화를 통한 서비스 관리 효율화


## MSA를 구현하는 기반 기술
- ![MSA 구현 기반 기술](https://velog.velcdn.com/images/dmchoi224/post/59bf02d3-2a2d-466c-83a6-67ace57ce5f8/image.png)
- ![서비스메쉬](https://github.com/Vailish/git-practice/assets/109258380/8edab10b-10ef-4774-9136-f4d199f1a9ed)
- ![service mesh](https://github.com/Vailish/git-practice/assets/109258380/d2746cd5-6d56-49e9-b53a-d3ed420bde57)


|Microservice Concern|Spring Cloud & Netflix OSS|Kubernetes|
|:---:|:---:|:---:|
|Configuration Management|Config Server, Consul, Netflix Archaius|Kubernetes ConfigMap & Secret|
|Service Discovery|Netflix Eureka, Hashicorp Consul|Kubernetes Service & Ingress Resources|
|Load Balancing|Netflix Ribbon|Kubernetes Service|
|API Gateway|Netflix Zuul|Kubernetes Service & Ingress Resources|
|Service Security|Spring Cloud Security|-|
|Centralized Logging|ELK Stack(Logstash)|EFK Stack(Fluentd)|
|Centralized Metrics|Netflix Spectator & Atlas|Heapster, Prometheus, Grafana|
|Distributed Tracing|Spring Cloud Sleuth, Zipkin|OpenTracing, Zipkin|
|Resilience & Fault Tolerance|Netflix Hystrix, Turbine & Ribbon|kubernetes Health Check & resource isolation|
|Auto Scaling and Self Healing|-|Kubernetes health Check & resource isolation|
|Packaging, Deployment & Scheduling|Spring Boot|Docker, Kubernetes Scheduler & Deployment|
|Job Management|Spring Batch|Kubernetes Jobs & Scheduled Jobs|
|Singleton Application|Spring Cloud Cluster|Kubernetes Pods|

## MSA 적용사례
- ![image](https://github.com/Vailish/git-practice/assets/109258380/b10cb569-eff2-40b7-8f11-be11bd0a1ce6)

### 국내 MSA 적용 사례
![국내 MSA 적용사례](https://velog.velcdn.com/images/dmchoi224/post/f2d444f9-2d01-4c09-aae4-9d759cf803da/image.png)


## MSA 구축 시 어려움
- ![MSA 구축시](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbhbHLX%2FbtrFuUT1miQ%2FzzXV6WFFL5mPFNYXGzBfs1%2Fimg.png)

- 왠만큼 복잡한 시스템을 사용하는 것이 아니라면, MSA는 불필요하며, 모놀리식이 더 낫다. - By MARTIN FOWLER (디자인 패턴 유명가)
- 복잡성이 높아야지만 모놀리식 대비 MSA의 생산성을 높이 가질 수 있겠다. 나의 기업 시스템 규모에 MSA의 생산성 효율을 따져봐야 할 것.

## Service Mesh 적용시 고려사항
- ![image](https://github.com/Vailish/git-practice/assets/109258380/b64a2971-b4c3-47e8-8dbd-57dd90987a0d)


## 참고자료
- [naver cloud talk&talk](https://www.youtube.com/watch?v=8d4h7K_Fq-0)
- [MSA란?](https://dodokong.tistory.com/63)
- [Microservice Architecture (MSA) 그리고 Monolithic](https://velog.io/@dmchoi224/Microservice-Architecture-MSA-%EA%B7%B8%EB%A6%AC%EA%B3%A0-Monolithic)
