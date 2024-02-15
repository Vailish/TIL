# Jira!

## Create issue
- Epic 생성시 다른 타입과 다르게 Epic Name 존재

## Components
- 사용하는 방법에따라 다름
- 역할, 역할 리더 등 설정
- ex) UX / 인프라

## JQL
- Jira Query Language
- Jira Issue를 구조적으로 검색 하기 위해 제공하는 언어
- SQL(Standard Query Language) 과 비슷한 문법
- Jira의 각 필드들에 맞는 특수한 예약어 들을 제공
- 쌓인 Issue 들을 재가공해 유의미한 데이터를 도출해 내는데 활용(Gadget, Agile Board 등)
- Basic Query VS Advanced Query

## JQL Operators
- =, !=, >, >=
- in, not in
- ~(contains), !~(not contains)
- is empty, is not empty, is null, is not null

## JQL Keywords
- AND
- OR
- NOT
- EMPTY
- NULL
- ORDER BY

## ex)
```JQL
project = "DP" issuetype = Epic and summary !~ 서버 ORDER BY created DESC

project = "DP" issuetype in (Epic, Story) ORDER BY created DESC
```

## JQL Dates
- Relative Dates

## JQL Functions
- endOfDay(), startOfDay()
- endOfWeek() (Saturday), StartOfWeek() (Sunday)
- endOfMonth(), startOfMonth(), endOfYear(), startOfYear()
- currentUser()

## JIRA의 기본적 활용
- Workflow
- BULK
- Components and Labels
- Releases

<br>

# Jira
- 들어가기 전에
- 현업에서는 무엇이 달라질까?
- App(Plugin) 활용
- 우수 사례
- Board 활용 예시
- 기타 유용한 기능

# 들어가기 전에
- 정답은 없다.
- 지표, 숫자에 집착 X, 편의를 위해 사용하는 것
- 주 목적은 잘 동작하는 제품

## 지라 사용시 장점
- 팀원들이 서로 무슨 일을 하고 있는지 파악 가능
- 변겨오딘 소스나 commit이 어떤 Issue와 관련 있는지 파악 가능
- 우리 팀의 제품 개발 진행이 원할 하다고 느껴짐
- Issue의 분류와 수치 산정 기준이 일관성 있음
- 이해하기 쉽고 직관적인 용어 사용

## 현업에서는 무엇이 달라질까?
- 기본적인 형태에서 필요한 부분을 커스텀해서 사용하는 정도
- Issue Types
- Field & Screen
- Work flow
- Log Works(Optional)

## Epic, Component, Label
- Epic
  - Issue들을 아우르는 큰 개념이 필요할 때
  - Issue Type 으로 관리할 필요성이 있을 때
- Component
  - 담당자/팀이 정해진 기능/범위가 있을 때
  - Default Assignee를 지정하고 싶을 때
- Label
  - 해시 태그 개념으로 접근
  - 대소문자, 공백에 유의

## Board, Sprint & Project
- Board, Sprint는 Project에 종속되어 있지 않다
- Issue에서 Sprint, Epic Link를 선택할 때 유의

# App(Plugin) 활용 (유료)
- Tempo Timesheets - Jira Time Tracking
- ScriptRunner for Jira
- eazyBI Reports and Charts for Jira

# 우수 사례
- story vs task
  - stroy : 나의 소프트웨어를 사용하는 사용자가 영향을 받거나 가치를 제공 받는 경우
  - task : 사용자가 직접적으로 영향을 받지 않는 경우
- Bulk Change
  - 이슈들을 한꺼번에 변경 가능
- Issue Export
  - xml, csv 등 뺄 수 있음, 이걸로 다른 jira 프로젝트에 옮기는 것도 가능
- Automation
  - GitLab과 연동하여 처리가능
  - API key 사용시 password가 아닌 Jira에서 생성 후 처리해줘야함