package com.vailish.db;

import java.util.stream.IntStream;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import com.vailish.db.entity.Memo;
import com.vailish.db.repository.MemoRepository;

@SpringBootTest
public class MemoRepositoryTest {
	
	@Autowired
	MemoRepository memoRepository;
	
	@Test
	public void InsertDummies() {
		
		IntStream.rangeClosed(1, 10).forEach(i -> {
			Memo memo = Memo.builder()
					.memoText("Sample..." + i)
					.build();
			//Create!
			memoRepository.save(memo);
		});
	}
}
