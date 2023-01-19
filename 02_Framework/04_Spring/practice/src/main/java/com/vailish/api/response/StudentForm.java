package com.vailish.api.response;

import com.vailish.db.entity.Student;

import lombok.Data;

@Data
public class StudentForm {
	private String name;
	private String major;
	
	public Student toEntity() {
		return Student.builder()
				.id(null)
				.name(name)
				.major(major)
				.build();
	}
}
//package com.vailish.api.response;
//
//import com.vailish.db.entity.Article;
//
//import lombok.Data;
//
//@Data
//public class ArticleForm {
//	private String title;
//	private String content;
//
//	
//	// 빌드를 사용하면, 아래와 같이 객체 생성 가능
//	public Article toEntity() {
//		return Article.builder()
//				.id(null)
//				.title(title)
//				.content(content)
//				.build();
//
//	}
//}
