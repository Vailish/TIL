package com.vailish.api.controller;

import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.vailish.api.request.Members;

@RestController
@RequestMapping("/api")
public class controller {
	
	@GetMapping("/test1")
	public String test() {
		return "안녕하세용";
	}
	
	@GetMapping("/test2")
	public ResponseEntity<Members> test2() {
		Members members = new Members();
		members.setId("777777");
		members.setName("vailish");
		members.setMajor("computer science");
		
		return new ResponseEntity<Members>(members, HttpStatus.OK);
//		return ResponseEntity.ok(members)
		
	}
}
