# Block Chain

## Cryptography
- 암호화
  - 복호화 가능
    - 대칭키 암호화
      - AES, DES, ...
      - ARIA, SEED
    - 비대칭키 암호화(공개키 암호화)
      - RSA, ECC
      - ECDSA
      - DS(전자서명)
  - 복호화 불가능(단방향 암호화)
    - SHA256, Keccak256, RIPEMD-160

### SHA256
### HASH FUNCTION

### Symmetric Encryption
- AES
- ARIA, SEED
![image](https://user-images.githubusercontent.com/109258380/222297063-6b9b959b-2209-4f63-9075-06656e9c494f.png)


### Asymmetric Encryption
- RSA
- ECC
![image](https://user-images.githubusercontent.com/109258380/222297172-dda398b7-95d2-4fef-adc5-86767f65f2f6.png)


## Digital Signature
-ECDSA
![image](https://user-images.githubusercontent.com/109258380/222297240-f396e9b6-a4f5-4d7e-ac96-3d3239a97160.png)


# Blockchain network
- 기본적으로 P2P(A peer-to-peer)
  - 서버가 아닌 각 컴퓨터간 연결
  - 토렌트와 같은 녀석도 있음

## How to work
![image](https://user-images.githubusercontent.com/109258380/222298307-e01289ed-1245-4515-9532-5672cab55d1c.png)

## Data in Block
![image](https://user-images.githubusercontent.com/109258380/222298787-e68e10b6-8ead-4a54-b832-4b32c5c3dcf7.png)

## Application
1. 결제 : 한계 - 느림, 가치변동성이 심함, 제약이 많음, 신뢰도(루나, 테라 사태)
2. 데이터 Storage : 암호화폐(송금 내역), 스마트 계약, 물류관리, 지역화폐, 문서관리, 의료정보관리, 저작권관리, 한정판 디지털상품(NFT), 소셜미디어 관리, 게임아이템관리, 전자투표, 신원확인 등
3. World Computing

## NFT(Non-Fungible Token)
- Unique(고유성)
- Only One(유일성)
- A scarcity value(희소성)

## Fully Decentralized vs Semi-Decentralized with Centralized Proxy
![image](https://user-images.githubusercontent.com/109258380/222300002-92b9413f-e69e-4d94-bc5f-4e50963186de.png)

## Summary
1. 블록체인은 보안성, 투명성, 무결성, 탈중앙화의 특징을 가지고 있고, 이 특징으로 여러가지 어플리케이션을 활용할 수 있다.
2. 블록체인의 네트워크는 기본적으로 P2P 네트워크에 작동한다.
3. 암호화에는 복호화 가능 암호화, 단방향 암호화로 나눠지고, 단방향 암호화는 해시함수로, sha256, keccak256등이 있다.
4. 암호화에 서명과 확인을 이용해 메시지의 무결성과 송신자를 보증하는 알고리즘을 전자서명이라고 한다.
5. 이 ECC암호화 알고리즘은 공개키 암호화로 타원 곡선 함수를 이용하여 암호화 한다.