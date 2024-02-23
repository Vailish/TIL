# Data Flow
- 왜 알아야 하는가?
- Data Flow 란?
- Data Flow 개념들
- Web Architecture 101
- Architect의 영역과 역할

# 왜 알아야하는가?
- 더 좋은 개발자가 되기 위해
- 보다 정확한 개발을 하기 위해
- 회의시간의 내용을 빠르게 이해할 수 있기 위해
- 개발 기간을 단축하기 위해

# Data Flow란?
- Presentation tier -> Logic Tier Application tier -> Data tier

# Data Flow 개념
## Monolithic Architecture of Three Tier
- 장점 : 세세하게 컨트롤 가능
- 단점 : 건드릴게 많음
![image](https://user-images.githubusercontent.com/109258380/221718180-8adf65c8-e85e-4887-96f5-bbf643498574.png)

## Micro Service Architecture
- 장점 : 편함
- 단점 : 수정하기 힘듬(컨테이너 내부)
- 먼저 monolithic을 사용해보고나서 docker를 사용한다면, 좀 더 감을 잡을 수 있어서 해결할 수 있는 역량을 갖출 수 있음 
![image](https://user-images.githubusercontent.com/109258380/221718535-ab753a6a-df77-4898-afaa-305a4d05e0c2.png)

## DevOps
![image](https://user-images.githubusercontent.com/109258380/221719712-a8c13152-fbf9-4961-ba2f-063e098fb1a8.png)

## Decentralization (BlockChain)
![image](https://user-images.githubusercontent.com/109258380/221719960-228e8446-556d-4f8f-92b2-81c0fa8b1f38.png)

## Summary
![image](https://user-images.githubusercontent.com/109258380/221720073-936842bf-1f16-4a24-8163-6286c086f0f5.png)

# Web Architecture 101
![image](https://user-images.githubusercontent.com/109258380/221720568-4c4d7410-0690-4d2f-bb5e-f91b821ce037.png)

- cf) MQ를 사용하는 이유 : 신뢰성보장, but 속도 포기

# Architect(설계자)의 종류와 역할
![image](https://user-images.githubusercontent.com/109258380/221721238-0f7510f5-2713-4809-bc55-9a47638a94f8.png)