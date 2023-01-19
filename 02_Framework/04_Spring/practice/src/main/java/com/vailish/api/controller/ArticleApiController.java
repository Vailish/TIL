package com.vailish.api.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.vailish.api.response.ArticleForm;
import com.vailish.db.entity.Article;
import com.vailish.db.repository.ArticleRepository;

import lombok.extern.slf4j.Slf4j;

@Slf4j  // lombok의 로깅 기능
@RestController
public class ArticleApiController {
	
	@Autowired
	private ArticleRepository articleRepository;
	
	@PostMapping("/api/articles")
	public Long create(@RequestBody ArticleForm form) {
		log.info(form.toString()); // 받아온 데이터 확인용
		
		// dto를 entity로 변경
		Article article = form.toEntity();
		
		// 레퍼지토리에 entity 전달
		Article saved = articleRepository.save(article);
		
		return saved.getId();
	}
}
