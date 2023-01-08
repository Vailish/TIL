package com.vailish.spring;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

//메이븐 : 빌드관리도구, 라이브러리세팅..
//         프로젝트 우클릭 > configure > convert to Maven Project
//메이븐에 문제가 있을시...
//1. alt + F5 update project. (플젝 우클릭 > 메이븐 > 업데이트 프로젝트)
//2. 상단메뉴 project > clean
//3. 이클립스 다 끄고, 사용자 > .m2폴더 삭제(파일에 1바이트라도 다르면 안되는 경우가 생기는데 이경우 찾기 힘드므로 지우고 다시켜서 다시 깔아주면 됨)

//메이븐을 통해서 프로젝트에 Spring 라이브러리 세팅
//    https://mvnrepository.com/ > spring 검색(spring core만으로 할 수 있지만 확장된 Spring context로 진행) > Spring Context
//     > 다운로드수가 많은(안정적으로 보이는 녀석, 여기서는 5.3.18) > Maven 복사해서 pom.xml의 build 뒤에 > <dependencies> 넣어주고
//     > 그 태그 안에 붙여넣기해서 dependencies 안에 dependency들을 넣어주면 됨

//스프링 설정파일 만들고 객체(bean) 등록하기/의존관계 설정
//스프링 컨테이너 객체 빌드, 사용
public class Test {
	public static void main(String[] args) {
		ApplicationContext
		context = new GenericXmlApplicationContext("applicationContext.xml");
		System.out.println("컨테이너 빌드 완료");
		//컨테이너로부터 내가 사용할 객체를 받아옴
//		Worker worker = (worker) context.getBean("worker"); //object니까 형변환해서 가져오기, 명시 안하면 기본값인 object로 줌
		Worker worker = context.getBean("worker", Worker.class); //이렇게 가져와도 됨
		Computer computer = context.getBean("desktop", Computer.class);
		System.out.println("두개의 갯빈 완료");
		worker.setComputer(computer);
		worker.doWork();
		//스프링 컨테이너는, 빈 객체들을, 언제 만들까?
		//1. 컨테이너가 만들어질 때(23번 라인), 정답
		//2. getBean을 달라할 때(26, 27번라인)
		
		//factory-method도 있음. 이는 Worker.java에 주석참조
		
		Worker worker2 = context.getBean("worker", Worker.class);
		//worker객체가 하나 더 만들어질까? 아니다. 안 만들어진다. 기본적인 정책은 singleton이다.
		//즉, 하나 생성한 뒤 참조함. 그래서 아래와 같이 true가 됨
		//lazy-init="true"를 applicationContext id 뒤에 넣어주면 무거워서 처음부터 안하고
		//필요할 때 호출함. 이럴 때는 컨테이너 빌드 후 생성자를 부름
		System.out.println(worker == worker2);
		//applicationContext에서 scope의 기본은 singleton이지만
		//scope="prototype"으로 둔다면, 부를 때 마다 새로 만들어 false가 나옴
	}
}
