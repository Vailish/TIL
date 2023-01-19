package com.vailish.api.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.vailish.api.response.StudentForm;
import com.vailish.db.entity.Student;
import com.vailish.db.repository.StudentRepository;

import lombok.extern.slf4j.Slf4j;

@Slf4j
@RestController
public class StudentApiController {
	
	@Autowired
	private StudentRepository studentRepository;
	
	@PostMapping("/api/student")
	public Long create(@RequestBody StudentForm form) {
		log.info(form.toString());
	
		Student student = form.toEntity();
		
		Student saved = studentRepository.save(student);
		
		return saved.getId();
	}
}