package com.vailish.spring;

import org.springframework.stereotype.Component;

//������ ���� ������ �׳� ������ Ŭ������ ù���� �ҹ���!
//�̸��� �����ָ� ������ �̸����� bean�� ��ϵ�!
//�������� �ΰ���, �����༮�ε� �̸��� �Ȱ��� �׷��� ������... �״ϱ� ���� �����̸�����
@Component("computer")
public class Labtop implements Computer{

	@Override
	public String getInfo() {
		// TODO Auto-generated method stub
		return "��Ʈ��!";
	}

}
