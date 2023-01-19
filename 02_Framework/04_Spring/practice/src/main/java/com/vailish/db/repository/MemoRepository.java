package com.vailish.db.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.vailish.db.entity.Memo;

public interface MemoRepository extends JpaRepository<Memo, Long>{

}
