# 데이터 사이언스와 데이터셋 활용
- 데이터 사이언스
- 데이터 사이언스 진행 과정
- 데이터 소스 대방출
- 데이터셋 살펴보기
- 데이터셋 활용과 사례
- 추천 시스템
- 더보기

# 데이터 사이언스
- why 데이터 사이언스?
  - 빅데이터의 시대
  - 데이터 기반 의사결정(DDDM)
  - 데이터 문해력의 중요성
  - 머신러닝은 데이터로부터 학습
- 데이터의 분석과 활용이 개인과 조직의 새로운 힘이 되고 경쟁력이 되는 시대
- 데이터 사이언스는 데이터 수집, 큐레이션,통계 분석과 기계학습 등의 다양한 기술과 지식을 활용하여 복잡한 데이터로부터 인사이트를 얻거나 지능화된 시스템을 구현하기 위한 모든 업무를 총칭
- 데이터 사이언스 로드맵

# 데이터 사이언스 진행 과정
1. 목표 설정 : 어떤 데이터와 리소스가 필요하고, 어떻게 이익을 내며, 일정, 최종 산출물 정의
2. 데이터 획득 : 사용할 데이터 존재여부(내부, 외부), 품질 정도, 접근 가능여부 파악 후 raw 데이터 확보
3. 데이터 정제(오류, 이상치, 결측지 등등..) 및 가공(변환, 조합)
4. 데이터 탐색 : EDA, 데이터에 대한 깊은 이해 및 해석(변수들의 상호작용, 데이터 분포), 시각화, 단순 모델링
5. 데이터 모델링 및 구축 : 도메인 지식, 통찰력으로 답을 찾는 과정, 모델 구축(변수선택)
6. 발표 및 자동화 : 경영진 발표, 연구 보고서, 업무 수행 과정 자동화

# 데이터 소스 대방출
- https://aihub.or.kr/
  - aihub 인공지능 학습용 데이터
    - 2023년 3월 현재 8개 분야 384종
    - 2025년까지 1300종
  - 한국어 데이터 93종
  - 영상이미지 데이터 78종
  - 헬스케어 데이터 67종
  - 농축수산 데이터 41종
  - 재난안전환경 데이터 59종
  - 교통물류 데이터 46종
- https://www.data.go.kr/
  - 공공 데이터 포털
    - 2023년 3월 현재 16개 분야 77,750종
  - 공공행정 13.4%
  - 문화관광 12.6%
  - 산업고용 9.4%
  - 교통물류 8.3%
  - 환경기상 7.8%
  - 재정금융 6.6%
  - 농축수산 6.4%
  - 국토관리 6.2%
  - 재난안전 5.3%
  - 과학기술 2.8%
  - 보건의료 5.3%
  - 식품건강 2.7%
  - 사회복지 5.9%
  - 교육 5.3%
  - 통일외교안보 1.5%
  - 법률 0.6%
- https://bigdata.seoul.go.kr/
- https://api.visitkorea.or.kr/
- https://www.findatamall.or.kr/
- https://kaggle.com/
- https://registry.opendata.aws/
- https://datasetlist.com
- https://towardsai.net/
- http://mlr.cs.umass.edu/ml/
- https://www.visualdata.io/
- https://data.oecd.org/
- https://www.datasetlist.com
- https://toolbox.google.com/
- https://paperswithcode.com/
- http://image-net.org
- https://storage.googleapis.com/openimages/
- https://towardsdatascience.com/
- https://github.com/dl0312/open-apis-korea
- https://github.com/yes973/Web Crawler
- https://open-apis.dev
- https://github.com/WooilJeong/PublicDataReader
- https://github.com/public-apis/public-apis
- https://guides.library.cmu.edu/machine-learning/datasets
- https://dsz.kdata.or.kr/svc/main/main.do
- https://data.kostat.go.kr/sbchome/index.do
- https://dacon.io/
- https://archive.ics.uci.edu/ml/datasets.php
- https://www.v7labs.com/open-datasets

# 데이터셋 살펴보기
1. 다이닝코드 맛집 데이터
  - 맛집 리뷰 데이터 : 45만건
  - 다이닝코드 : https://www.diningcode.com/
2. 카드사 데이터
  - 금융소비 리뷰 데이터 : 5,400만건

## 맛집 데이터
- 기본 음식점 기본 POI 데이터 : 전국 45만개의 매장 정보 식당명, 지점명, 주소, 전화번호, 위도, 경도, 위치명, 카테고리 정보
- 전국 음식점 메뉴 및 운영시간 데이터 : 22만 개 매장의 판매 음식 정보 메뉴 및 운영시간 데이터
- 전국 음식점 리뷰 데이터 : 4만 5천개 매장의 리뷰 데이터, 총 9만 건의 리뷰 사용자 및 별점
- 리뷰 작성 사용자 데이터 : 리뷰 작성 사용자의 기본 데이터(성별 및 연령 정보)

## 금융소비 데이터
- 금융소비 데이터는 개인식별 불가한 데이터로 다른 데이터와 조인하여 사용하기를 권장
- 데이터 세부 정보
  - 회원_시도명
  - 개인기업구분(개인회원 또는 법인회원)
  - 성별(남/여/외국인)
  - 연령(10세 단위)
  - 매출년월일(형식:YYMMDD)
  - 승인시각대(1시간 단위)
  - 이용건수(정상/취소 상계처리 결제 건수 합)
  - 결제금액(정상/취소 상계처리 결제 금액 합)
  - 가맹점_시도명
  - 가맹점_시군구명
  - 가맹점_읍면동(행정동 또는 법정동 단위)
  - 가맹점업종코드(카드사 분류 업종코드)


# 학습 로드맵(추천 시스템)
 ![image](https://user-images.githubusercontent.com/109258380/222601685-3417bd95-6ac8-45e0-8762-477d178eaf9e.png)

# 빅데이터 학습 자료
![image](https://user-images.githubusercontent.com/109258380/222601963-00a9b13e-6351-49a8-9da8-34aff857f672.png)

# 추천 시스템 목적
- 특정 시점에 특정 고객(user)이 좋아할 만한 상품(item)을 찾아주는 것
- 추천 모델링 : 유저 정보 + 로그 데이터 + 아이템 정보

![image](https://user-images.githubusercontent.com/109258380/222602140-e6c90896-29c7-45dc-95d8-6341911ad295.png)

# 주요 알고리즘(추천)

![image](https://user-images.githubusercontent.com/109258380/222602225-03d9c0fc-19b7-4cda-b763-b799f2fc8d35.png)

# 추천 시스템 효과
- 좋은 경험을 제공하여 서비스 만족도 향상
- 회전율과 체류시간을 높여 고객 이탈 방지

# 좋은 추천 결과(성능)를 얻기 위해서는?
- 데이터에 대한 이해 통찰력
  - 어떤 값이 어떤 수치로 표현되어 있나?
  - 특성들 사이에는 어떤 관계가 있나?
- 모델(추천 알고리즘)에 대한 이해
  - 알고리즘 별 특징과 장단점은?
  - 상황 별 알고리즘 적용법은?

