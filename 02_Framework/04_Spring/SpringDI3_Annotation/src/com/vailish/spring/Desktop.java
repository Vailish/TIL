package com.vailish.spring;

import org.springframework.stereotype.Component;

//@Component // component�� ����ϸ� ���� �����ܿ� S�ڰ� �����!
public class Desktop implements Computer{

	@Override
	public String getInfo() {
		// TODO Auto-generated method stub
		return "����ũž!";
	}

}
