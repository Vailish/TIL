package com.vailish.db.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Getter
@ToString
@NoArgsConstructor
@Entity
public class Student {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY) // DB생성시 1씩 증가
	private Long id;
	
	@Column(length = 100, nullable = false)
	private String name;
//	 default 'EMPTY'
	@Column(columnDefinition = "varcahr (20)", nullable = false)
	private String major;
	
	@Builder
	public Student(Long id, String name, String major) {
		this.id = id;
		this.name = name;
		this.major = major;
	}	
}
