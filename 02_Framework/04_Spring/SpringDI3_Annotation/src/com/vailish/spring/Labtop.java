package com.vailish.spring;

import org.springframework.stereotype.Component;

//낙인을 찍을 찍을때 그냥 찍으면 클래스명 첫글자 소문자!
//이름을 정해주면 정해준 이름으로 bean이 등록됨!
//선택지가 두개다, 같은녀석인데 이름도 똑같음 그러면 오류냄... 그니까 쓸걸 같은이름으로
@Component("computer")
public class Labtop implements Computer{

	@Override
	public String getInfo() {
		// TODO Auto-generated method stub
		return "노트북!";
	}

}
