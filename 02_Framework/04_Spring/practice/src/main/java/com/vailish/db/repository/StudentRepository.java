package com.vailish.db.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.vailish.db.entity.Student;

public interface StudentRepository extends JpaRepository<Student, Long> {

}
