package com.ssafy.controller;

import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

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
		return "hi rest";
	}
	
	@GetMapping("/test3")
	public Map<String, String> test3() {
		Map<String, String> data = new HashMap<String String>();
		
		data.put("id", "Dev");
		data.compute("name", "베일리쉬");
		data.put("password", "1234");
	}
}
