package com.ssafy.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.model.dto.Member;

@RestController  // 이녀석을 쓰면 Responsebody는 필요 없다!
@RequestMapping("/rest2")
public class TestController2 {
	
//	http://localhost:8080/mvc/rest2/test1 - 404에러...
	@GetMapping("/test1")
	public String test1() {
		return "hi rest";
	}
	
//	http://localhost:8080/mvc/rest2/test1
	@GetMapping("/test2")
	public String test2() {
		System.out.println("test2 성공!");
		return "hi rest";
	}
	
//	http://localhost:8080/mvc/rest2/test3
	@GetMapping("/test3")
	public Map<String, String> test3() {
		Map<String, String> data = new HashMap<String, String>();
		
		data.put("id", "Dev");
		data.put("name", "베일리쉬");
		data.put("password", "1234");
		
		return data;
	}

//	http://localhost:8080/mvc/rest2/test4
	@GetMapping("/test4")
	public Member test4() {
		Member m = new Member();
		m.setId("Dev");
		m.setName("Snow");
		m.setPassword("1234");
		
		return m;
	}
	
//	http://localhost:8080/mvc/rest2/test5
	@GetMapping("/test5")
	public List<Member> test5() {
		List<Member> list = new ArrayList<>();
		for(int i = 1; i < 5 ; i++) {
			Member m = new Member();
			m.setId("Dev" +i);
			m.setName("Snow" +i);
			m.setPassword("1234");
			list.add(m);
		}
		return list;
	}
}
