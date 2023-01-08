package com.vailish.spring;

import org.springframework.stereotype.Component;

//@Component // component로 등록하면 좌측 아이콘에 S자가 생긴다!
public class Desktop implements Computer{

	@Override
	public String getInfo() {
		// TODO Auto-generated method stub
		return "데스크탑!";
	}

}
