# DBeaver와 CMD를 사용한 MariaDB 백업 복구
## MariaDB란?
MariaDB는 오픈 소스의 관계형 데이터베이스 관리 시스템(RDBMS)이다. MySQL과 동일한 소스 코드를 기반으로 하며, GPL v2 라이선스를 따른다. 오라클 소유의 현재 불확실한 MySQL의 라이선스 상태에 반발하여 만들어졌으며, 배포자는 몬티 프로그램 AB(Monty Program AB)와 저작권을 공유해야 한다
## 1. 데이터테이블 만들기
```sql
create database singer;

create table singer.datas (
	generation int not null,
	numbers int not null
);
 
create table singer.group (
	name varchar(20) not null,
	group_member int not null
);

insert  into singer.datas
values
	(1, 100),
	(2, 100),
	(3, 300),
	(4, 500),
	(5, 700),
	(6, 900),
	(7, 1000),
	(8, 850);

insert into singer.group
values
	('트와이스', 6),
	('아이유', 1),
	('노라조', 2),
	('볼빨간사춘기', 2),
	('악뮤', 2),
	('이하이', 1),
	('다비치', 2),
	('비스트', 6),
	('동방신기', 2),
	('소녀시대', 9),
	('배치기', 2);
```

## 2. 관리자 권한으로 CMD를 켜서 full backup하기
```cmd
mariadb-dump -u root -p --all-databases > ssafy_backup_all.sql
```

![image](https://user-images.githubusercontent.com/109258380/209601128-79979217-9150-4a05-bc91-f722be949d38.png)

## 3. 삭제하기
```sql
drop database singer;
```
![image](https://user-images.githubusercontent.com/109258380/209601593-7a08f865-eae2-4d4d-92e7-db031d201432.png)

## 4. CMD로 복구하기
```cmd
mariadb -u -root -p < singer_backup_all.sql
```
![image](https://user-images.githubusercontent.com/109258380/209601750-68e5861b-5501-4cb4-bb5b-b5716d020b64.png)

![image](https://user-images.githubusercontent.com/109258380/209601817-a3a4afe2-6507-4ce5-8941-a1f388264819.png)

## 5. cmd로 table backup하기
```cmd
mariadb-dump -u root -p singer datas > singer_backup_datas_table.sql
```

![image](https://user-images.githubusercontent.com/109258380/209602034-0c04eec8-4999-400f-84ba-a2632dd63a4f.png)

## 6. table drop & restore
```sql
drop table singer.datas;
```

![image](https://user-images.githubusercontent.com/109258380/209602306-730b5e72-35fa-4a88-bb73-a8d3c2bd4d3c.png)

![image](https://user-images.githubusercontent.com/109258380/209602418-ffb0c74c-521e-464e-ad3d-301787b970d5.png)

![image](https://user-images.githubusercontent.com/109258380/209602459-dc3ccc40-5c4c-4190-8a70-a8bd0ba42acb.png)

## 7. binary log 복구, my.ini 추가
![image](https://user-images.githubusercontent.com/109258380/209602591-ac3b4bf9-7817-437c-a565-f15bb7162217.png)

## 8. 마리아DB 재실행하기
![image](https://user-images.githubusercontent.com/109258380/209602702-4174f281-65f5-4a44-8139-d5efdf983048.png)

## 9. data삭제 및 binary log파일 확인
```sql
delete from singer.datas
where generation < 7
```
![image](https://user-images.githubusercontent.com/109258380/209602901-cb95ef90-69dd-42ca-8d69-6a68bd1c088c.png)

![image](https://user-images.githubusercontent.com/109258380/209602968-e23843b7-cf09-4d0b-984e-4333ba6ac2c1.png)

## 10. sql 파일 생성 및 이슈 쿼리 확인
```cmd
mysqlbinlog --database=singer --start-datetime="2022-12-27 11:40:00" --stop-datetime="2022-12-27 11:46:00" > singer_binlog.sql
```
![image](https://user-images.githubusercontent.com/109258380/209603286-9dceb009-335d-43de-9e81-9648296d1a02.png)

![image](https://user-images.githubusercontent.com/109258380/209603460-94b4371c-4f33-40d7-9986-30e88b62b50c.png)