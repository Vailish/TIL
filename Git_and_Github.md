# Git, Github

### Git & Github

- Git : 분산 버전 관리 프로그램 - 데이터 보존에 유리(<->- 중앙집중식, ex) SVN / 예전에는 많이 썼지만 요즘은 잘 안씀
)
  - **백업+복구+협업** : 육하원칙으로 정리해주니까 협업이 가능해짐 - 단/ 이유파트는 사람이 직접!
    - 백업 : add, commit
    - 복구 : reset, revert
    - 협업 : push, pull, clone, branch, merge
  - Git != Github
    - Github는 Git을 사용하는 저장소 즉, Git 내pc Github
    - git
      - Working Directory : 사용자의 작업영역 (add를 통해 staging area로 넘김)
      - staging Area : commit을 위한 파일 및 폴더들이 위치하고 있는 영역(commit후 repository로 넘김)
      - Repository : 저장된 파일이 있는 영역(push를 통해 깃허브에 넘김)

##### Git을 하면서 많이 하는 실수

- submodule : git 속 git 
  - git 관리하는 폴더 안에 다른 폴더를 만들어서 git을 또 init 하는 경우
  - 현업에서도 잘 사용 안 하는 어려운 내용, 언젠가 에러가 날 수 있음
- 바탕화면에서 여는 경우 
- Github 안에서 파일 드래그해서 올리는 경우
  - 먼저 이렇게 수정하면,  working direction이랑 github랑 버전이 달라서 오류가남.

##### README.md & .gitignore

git and readme

- readme.md : Github 대문, 반드시 대문자로 써야함
- .gitignore
  - 이 안에 파일명 넣어주면 그 파일들의 git이 관리를 안해줌(올리고 싶지 않은 녀석하면됨)
  - 남에게 보여주면 안되는 보안파일(개인정보, Key값 등, 해킹 우려있음.)
  - 굳이 올리지 않아도 되는파일(ex)용량이 엄청 큰 모듈에 있어 쓰레기파일 등)
  - 이미 push해서 밀어 넣은 파일은 후에 .gitignore 넣어도 의미가 없음, **이미 버전관리 하고 있기때문에 무시 할 수 없음. 무르기 안됨**, 그러므로 .gitignore은 맨처음에 만들자!
  - 앞에 . 을 붙이면 숨은파일
  - VSC에서 아이콘 붙여줘서 특수파일임을 분류해줌. - README.md도 마찬가지
  - gitignore.io : 여기에서 사용할 프로그램을 입력해주면 알아서 쓰레기파일 등 ignore할 것을 작성해줌 ex) python, windows, Visual Studio Code  처럼 입력해주면 됨.

##### Git
- status : "3공간"의 상태
- git log : version(commit)의 상태

##### Clone & Pull

- clone : 다운로드

  - git clone [원격저장소URL]
    - 폴더생성
    - git init
    - git remote add
    - version, file 생성
    - 폴더를 놓을 위치에서 git bash here 후 git clone URL 하면 됨.(키보드 단축기 불가, 마우스 우클릭 활용가능)
      - 만약에 폴더를 만든 다음에 들어가서 코드로 열어서 git clone으로 하게되면, 폴더가 중첩되어서 원하는데로 안 될 수 있음.

- pull : 업데이트

  - git pull origin master

  - 정상적으로 push & pull 하면 되지만, 아닌 경우 오류가 나옴!

    | -        |          |                                                                                           | 이 경우 오류(CONFLICT) | 선택해서 올림 |
    | -------- | -------- | ----------------------------------------------------------------------------------------- | ---------------------- |
    | version1 | version2 | version3                                                                                  | version4               |
    |          |          | version3                                                                                  |                        |
    |          |          | 허브에는 신규버전이 있는 상황에서 다른 곳에서 신규버전을 만들어서 add하려면 나타나는 오류 |                        |

    - ![](20220715.assets/error_pic.png)
  
    - 오류 나올때 pull로 받으면 두개다 나와서 필요한 거 남기고 지우거나 새로 쓰면 됨.
  
      - VSC에서는 오류 나올때 pull로 받으면 둘 중 하나 선택 하게끔 색으로 구분해서 동시에 보여줌, 클릭하면 됨.
      - 다 하고나서 Version4로 합쳐야 하기 때문에 unmering으로나옴 그러므로 add 부터 다시 진행하면됨.
        - 그래서 Commit을 보게 되면, 각각의 version3의 commit이 둘 다 표시됨. 그래서 merging이라는 표현을 쓰게됨.
  
- git log --online : local commit(version) 확인방법

- 협업시 권한부여

  - 팀장 : Github - 새 폴더생성 setting collaborators -> add people
  - 팀원 : email 승인

  - 설정한 폴더만 권한을 주고 가짐

- branch & merge : 협업 규모가 커지면 이를 이용하여 처리함

  - push & pull 같은 경우에는 개인, 혹은 소규모일 때 유용함.



- git branch 관련
https://eunhee-programming.tistory.com/256