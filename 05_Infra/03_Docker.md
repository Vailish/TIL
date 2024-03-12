# Docker

## Docker CLI
- [Docker CLI Docs](https://docs.docker.com/reference/cli/docker/)

- 컨테이너 확인
```bash
docker ps -a
```

- 이미지 확인
```bash
docker images
```

- 이미지 삭제
```bash
docker rmi [이미지아이디]
```

- 컨테이너 삭제
```bash
docker rm [컨테이너아이디]
```

- 컨테이너 이름 변경
```bash
docker rename [컨테이너이름] [변경할이름]
```

- 컨테이너 생성 및 실행
```bash
$ docker run --name frontend -d -p 3000:3000 frontend
```

- 컨테이너 접속
```bash
docker exec -it mysql-container bash
```

- mysql 컨테이너 실행
```bash
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -d -p 3306:3307 mysql
```

## Docker를 이용한 배포
- [Docker-Spring-프로젝트를-Docker를-이용해서-배포해봅시다](https://velog.io/@18k7102dy/Docker-Spring-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EB%A5%BC-Docker%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C-%EB%B0%B0%ED%8F%AC%ED%95%B4%EB%B4%85%EC%8B%9C%EB%8B%A4)

### Dockerfile
```dockerfile
# 베이스 이미지 지정, 베이스 이미지와 태그를 지정하면 registry(docker hub)에서 해당 이미지를 가져옴(Pull)
FROM openjdk:21-alpine  # openjdk alpine 21버전 실행하겠다.

ARG JAR_FILE=build/libs/*.jar  # JAR_FILE 변수 정의

COPY ${JAR_FILE} app.jar  # JAR_FILE 메인 디렉토리에 복사

EXPOSE 8080  # 포트는 8080으로 하겠다.

ENTRYPOINT ["java", "-jar", "/app.jar"]  # 시스템 진입점 정의
```

## 시나리오
1. 테스트용 스프링 빌드
    - jdk 21
    - intellij 기준 우측의 Gradle -> build -> build 더블클릭 ->./build/libs/springServer-0.0.1-SNAPSHOT.jar
2. 빌드한 파일 실행
```bash
java -jar 파일
```
3. 빌드한 파일을 바탕으로 docker 이미지화
4. 이미지화한 docker파일을 docker hub에 올림
5. Docker에서 컨테이너 하나 만든다음에 해당 컨테이너에 해당 프로젝트를 가져옴
6. 필요한 사항 세팅
7. 프로젝트 실행 및 테스트
