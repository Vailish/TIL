package com.ssafy.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.ssafy.model.dto.Member;

@Controller
@RequestMapping("/rest1")
// 좌측에서 property - project setting - root가 mvc이므로
// http://localhost:8080/context-path/rest1 ->
// http://localhost:8080/mvc/rest1
public class TestController1 {
	
//	http://localhost:8080/mvc/rest1/test1 - 404에러...
	@GetMapping("/test1")
	public String test1() {
		return "hi rest";
	}
	
//	http://localhost:8080/mvc/rest1/test1 - ResponseBody
//	붙이는 순간 JSP 화면같은 것이 아니라 반환값 그 자체를 데이터로 넘김
	@GetMapping("/test2")
	@ResponseBody
	public String test2() {
		System.out.println("test2 성공!");
		return "hi rest";
	}
	
//	http://localhost:8080/mvc/rest1/test3
	@GetMapping("/test3")
	@ResponseBody
	public Map<String, String> test3() {
		Map<String, String> data = new HashMap<String, String>();
		
		data.put("id", "Dev");
		data.put("name", "베일리쉬");
		data.put("password", "1234");
		
		return data;  // JSON으로 변환해줘 -> 406 -> mvn에서 Jackson databind pom에 등록하면됨
	}
	
	@GetMapping("/test4")
	@ResponseBody
	public Member test4() {
		Member m = new Member();
		m.setId("Dev");
		m.setName("Snow");
		m.setPassword("1234");
		
		return m;
	}
	
	@GetMapping("/test5")
	@ResponseBody
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
