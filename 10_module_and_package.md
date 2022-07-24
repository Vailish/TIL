##### 사용자 모듈과 패키지
- 모듈 < 패키지 < 라이브러리
- 모듈(module) : 다양한 기능을 하나의 파일로
- 패키지(package) : 다양한 파일을 하나의 폴더로
- 라이브러리(library) : 다양한 패키지를 하나의 묶음으로
  - cf) 프레임워크 : (버즈워드 : 논란의 여지가있음) 교수님의 경우 포크레인(라이브러리 : 삽)
  - 둘 다 사용해서 이용하지만, 라이브러리는 주도권이 나에게 좀 더 있고, 프레임워크는 내가 시키는데로 하긴하지만 주도권은 없다, 자유롭게는 못씀
  - pip : 라이브러리를 관리하는 관리자
  - package의 활용 공간 : 가상환경

##### 모듈과 패키지
- 모듈 : 특정 기능을 하는 코드를 파이썬(.py) 단위로 작성한 거
- 패키지
  - 특정 기능과 관련된 여러 모듈의 집합
  - 패키지 안에 또 다른 서브 패키지를 포함
- 모듈과 패키지 불러오기
  - import module
  - from module imort var, function, class
  - from module import *
  - from package import module
  - from package.module import var, function, Class

##### 파이썬 표준 라이브러리
- 파이썬에 기본적으로 설치된 모듈과 내장 함수
  - https://docs.python.org/ko/3/library/index.html
- 파이썬 패키지 관리자(pip)
  - PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
  - 패키지 설치 (bash, cmd 환경에서 사용되는 명령어)
    - $ pip install SomePackage <- 최신 버전
    - $ pip install SomePackage==1.0.5
    - $ pip install 'SomePackage>=1.0.4'
  - 패키지 삭제
    - pip는 패키지 업그레이드를 하는 경우 과거 버전을 자동으로 지워줌
    - $ pip uninstall SomePackage
  - 피키지 목록 및 특정 패키지 정보
    - $ pip list <- 설치된 목록
    - $ pip show SomePackage <- list보고 자세히 알고싶은거
  - 패키지 관리하기 - 파이썬 패키지 관리자(pip) 명령어
    - $ pip freeze > requirements.txt <-목록을 관리, 목록을 박제(하고 나중에 다른 곳가서 install을 통해서 이어서할 수 있음)
    - $ pip install -r requirements.txt <- 목록을 설치
    - 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함

##### 가상환경
    - 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치해야함
    - 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
      - 과거 외주 프로젝트 - django 버전 2.x
      - 신규 회사 프로젝트 - django 버전 3.x
    - 가상 환경을 만들고 관리하는데 사용되는 모듈(Python 버전 3.5 부터)
    - 특정 디렉토리에 가상환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
      - 특정 폴더에 가상환경이(패키지 집합 폴더 등) 있고
      - 실행 환경(예 - bash)에서 가상환경을 활성화 시켜
      - 해당 폴더에 있는 패키지를 관리/사용함
    -  pip list <- 설치된 환경 검색 (윈도우랑 맥이랑 조금 다름, 여기선 window 기준)
       - python -m venv venv : 가상환경 설정
       - venv폴더 생성됨 -> 이 폴더에 필요한 것 설치가능
       - -> sourse venv/scripts/activate -> 좌측 영역에 가상환경 설치된 것, 그래서 이때 여기서 list를 치면 두 개만 설치된 것을 볼 수 있음.
       - -> pip install -r requirements.txt 이런식으로 설치

##### json 파일 이용
open(a, b, ~) <- a : 문자열!!을 받음
ex) open('sample.json', encoding='utf-8') <- 'sample.json' 앞에 .\이 생략된거임 .\는 자기와 같은 위치  //utf-8이라는 인코딩 방식으로

 json : python의 dictionary와 비슷함 -> python에서 쓰려면 dictionary로 바꿔줘야함.

pprint() <- 예쁘게 출력해줌(가독성 있게) : 2차원 list나 dictionary 등

if __name__ == '__main__': - 파일 직접 실행하는 거 아니면 실행하지마라~~
