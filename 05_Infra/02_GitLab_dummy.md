# GitLab

## 설치 과정

### GitLab 가이드
- [GitLab_README](https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/README.md)
- 

## 참고사이트
- [블로그 - GitLab-깃랩-우분투Ubuntu서버에-세팅](https://sm-code.tistory.com/entry/GitLab-%EA%B9%83%EB%9E%A9-%EC%9A%B0%EB%B6%84%ED%88%ACUbuntu%EC%84%9C%EB%B2%84%EC%97%90-%EC%84%B8%ED%8C%85)

## 개념
## GitLab CE VS EE
- GitLab CE
    - 무료
- GutLab EE
    - 유료
    - 유료티어 업그레이드 가능
- [Infograb - GitLab CE vs EE](https://insight.infograb.net/docs/about/gitlab_ce_ee/)

### GitLab CE 사용하는 이유
- 오픈 소스 소프트웨어 기능만 사용하려는 경우 Community Edition이 최선의 선택입니다. 이 배포에는 독점 코드가 포함되어 있지 않습니다. 기능적으로는 라이선스 키가 없는 Enterprise Edition과 동일하게 작동합니다.
- 향후 Enterprise Edition으로 전환하기로 결정한 경우, 업그레이드가 필요하며 다운타임이 필요할 수 있습니다.

### 라이선스 키 없이 GitLab Enterprise Edition을 설치한 경우, 일반적인 Community Edition 인스턴스와 동일한 기능을 모두 사용할 수 있으며, 추가 이점이 있습니다.

언제든지 유료 기능을 평가하고 싶다면, 새 인스턴스를 설치 및 구성하거나 기존 인스턴스를 업그레이드하지 않고도 이 작업을 수행할 수 있습니다. GitLab 내에서 평가판을 활성화하기만 하면 됩니다. 유료 기능에 만족하지 않는 경우 평가판이 만료된 후 인스턴스가 자동으로 무료 기능으로 되돌아갑니다.

Community Edition을 사용하는 경우 유료 티어로 업그레이드하려면, Community Edition에서 Enterprise Edition으로 마이그레이션이 필요하며 다운 타임이 필요한 특정 단계를 따라야 합니다. Enterprise Edition을 사용하는 경우 클릭 한 번으로 유료 기능으로 업그레이드할 수 있습니다.

- [GitLab Premium](https://insight.infograb.net/docs/about/gitlab_license_premium/)
    - CI/CD 쪽 편의성
- [GitLab Ultimate](https://insight.infograb.net/docs/about/gitlab_license_ultimate/)
    - 보안 강화

![요금제](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FS7d7p%2Fbtrv3gecuAg%2FRJawpDaV75SQheZsESpHhk%2Fimg.png)



## 진행순서

### 이거보고 진행함
- https://ux.stories.pe.kr/161

### postfix 에러 해결
- https://freesunny.tistory.com/5

### vim
- https://secretpoten.tistory.com/99

### 방화벽 on / off
```
yum install firewalld
systemctl enable firewalld 
systemctl start firewalld // on
systemctl stop firewalld // off
```

### gitlab-ctl
```bash
gitlab-ctl stop
vi /etc/gitlab/gitlab.rb
gitlab-ctl reconfigure
gitlab-ctl start
```

### 최소사양
- 4vCPU 4GB RAM
- https://docs.gitlab.com/ee/install/requirements.html