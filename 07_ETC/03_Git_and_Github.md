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

git 초기 설정

- git config --global user.name "이름" : 커밋의 기록을 위한 username

- git congig --global user.email "메일 주소" : 커밋의 기록을 위한 username
  
- 설정 확인법
- 
  - git config --global -l

  - git config --global --list

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

---

- git branch 관련
https://eunhee-programming.tistory.com/256

Git - 분산 버전 관리 프로그램 - 데이터 보존에 유리(<->중앙집중식)
     ->백업+복구+협업(육하원칙으로 정리해주니까/이유는제외)
백업 add, commit
복구 reset, revert
협업 push, pull, clone, branch, merge
Git /= GItHub(Git을 사용하는 저장소)
내PC   올려서 공유

네이버, 카카오 등 대규모 회사에서는 소스코드 등이 엄청 많기 때문에
Git과 같은 프로그램이 중요하고 필요함


포트폴리오 = 증명이다, 그래서 GitHub가 중요함. 1일 1commit
window키랑 화살표 - 화면분할
리누스 = 리누스랑 Git만듦

------------------------------------------------------------------------------------
<<<CLI>>>
 ->Git Bash로
Interface : 두가지가 만나는 접점을 말함 ex) HDMI
CLI : Command Line Interface
GUI : Graphic User Interface

mkdir(make directory, 폴더생성) ex) mkdir test
ls(list segment, 니 있는곳 리스트로 뽑아라) ex) ls
cd(change directory, 이동)
cd ..(뒤로가기)
-절대경로 : 고유주소  ex) C : root
-상대경로 : ex) 기준점 옆에 cd test(내가 있는곳에서 test폴더로)   // .나  ..부모

touch : 파일 생성 ex) touch a.txt
rm : 파일 삭제(폴더는 안됨 아래 r처럼 옵션 넣어줘야함)
ctrl l : 아래로 내리기(깔끔히 볼때)
r(recursive 재귀적인, 옵션?) ex) rm -r a (a폴더를 삭제하라)
ls -a : 숨긴 파일까지도 싹다 보여주는것

## https://www.w3schools.com/whatis/whatis_cli.asp
--------------------------------------------------------------------------------------

Markdown : 텍스트 기반의 경량 마크업 언어
 -> Typora로

마크업 -> 역할을 부여하는 (마크하는) 것
 -> markdown은 markup 언어의 일부
ex) <제목> 싸피 8기 입학 현장 <제목>
ex) html의 <h3> 싸피 8기 입학 현장 <h3>

# -> 제목으로 #~###### 까지 가능
ctrl / = 날것 그대로 다 보여줌

- 목록으로 목록 안에 목록 가능(문양은 못바꿈)
1.숫자목록 안에 넣을거면 tab
** 굵게 **
* 기울임 *
~~취소선~~
`print("hello world")` 인라인 코드 (너 코드야)
```python : 코드언어 지정
--- 수평선

표
우클릭으로 표   <- typora를 쓰는 이유
ctrl enter 줄 삽입
ctrl shift backspace 줄 삭제

3. 마크다운 문법에서 글씨의 크기를 키우고 싶다고해서 본문을 제목으로 지정하면 안된다. (맞으면 O, 틀리면 X)
   - 답 : O
   - 이유 : 마크다운은 글에 역할을 부여한다. 디자인이 아니다.

---
<<<Git>>>
git config --global user.name vailish 이름 등록해줘
git config --global user.email ABC@gmail.com 이메일 등록해줘
git config --global --list 리스트 보여줘
git init : 이거 git으로 가입할거야 (일반폴더를 git이 관리하는 로컬 저장소로 만들자!)
ls -a : .git이 나오면 git이 관리해주고 있는거
누구(한번하면 그 컴퓨터에서 안해도됨) -> 초기화 -> 3공간 -> 버전
git status : 상태보기(등록했나 안했나 확인) / 아래 한 번 더썻음

"Git 로컬저장소" : 
WD(working directory)(작업폴더)[붉은색] - git add-> SA(staging area준비)[초록색] -git commit> commit (=status)(업로드/공유)
Staging area가 있는 이유
 1. 원하는 것들 만으로 업데이트 하기위해서

SA에 올려놧는데 WD에서 지워버리면 녹색(new file)과 빨간색(deleted) 같이 나옴
 -> 지운것도 변경사항이니까 같이 올라오는거

git add : git에게 넘기는거
git add . : 현 폴더 전체 등록
git commit -m "first commit" - first commit : 왜 라는 부분 내가 쓰는것
git status : 전반적인 상태 -> 중요! , 내가 add를 쓸지 commit을 칠지 다 된건지 알 수 있기때문에
git log : 버전의 상태

git 버전관리는 프로젝트 제일 최 상단에서 하는것 연결경로를 보면됨.
고로 Git practice라는 폴더 안에서 a.txt랑 b.txt를 관리한다면 이때의 버전은 각각의 파일이 아닌
폴더 자체의 버전임.


commit 2bf3ecb9f16448cb5c74552daa1cd01e918f5c4e <- 커밋ID, 해시값(고유한 번호, 어떠한 경우도 겹치지않음 -> 이걸 기준으로 버전을 되돌릴 수 있음)
Author: vailish <ABC@gmail.com>
Date:   Thu Jul 14 15:35:48 2022 +0900

    second commit


git checkout 2bf3ecb9f16448cb5c74552daa1cd01e918f5c4e(돌아가고싶은 버전 주소) : 이 commit으로 돌아가볼까? (지운거 아님)
git rest --hard 2bf3ecb9f16448cb5c74552daa1cd01e918f5c4e(최신버전주소) 이 버전으로 돌아가자(원래버전)

ctrl C 중간에 줄바꿔서 진행 못할때 탈출 가능

깃허브에 올리려면 로컬과 깃허브 사이에 길을 만들어줘야함
local -git push-> remote

git remote add origin https://github.com/Vailish/TIL.git <- 이건 깃주소(여기에 추가로 Origin이 이제 옆주소가 되는거)
git remote -v : 확인
git push origin master 넘기기

로컬에서 다한다음에 넘겨주기까지해야됨

git rm -> commit 자체를 지워버림 -> 직전 버전으로 돌아감
git restore -- staged commit을 지우는 것이 아니라, staged 주소값을 직전 값으로 바꾸어 줌 -> 직전 버전으로 돌아가는 효과

working directory와 staging area는 공유하기 때문에 branch 스위치 하기전에는 무조건 커밋을 다 하고 변경하자...


1. git graph 설치

2. commit 3개

3. 브랜치 조회