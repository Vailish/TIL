# Ubuntu
## Docker 환경에서 Ubuntu 설치하기
## Sudo 설치
- 오류 `-bash: sudo: command not found`
- 설치 확인
```bash
dpkg -l sudo
```
- root 계정
```bash
su -
```
- sudo 설치
```bash
apt-get install sudo -y
```




### 참고자료
- [블로그 - [도커] Windows 10에서 도커로 우분투 설치하기](https://hwan-shell.tistory.com/178?category=858112)
- [sudo 설치(-bash: sudo: command not found 오류 메세지 해결법)](https://blog.naver.com/greenysky/222876167226)