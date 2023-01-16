package com.vailish.hello;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class HelloSpringBoot2Application {

	public static void main(String[] args) {
		ApplicationContext context = SpringApplication.run(HelloSpringBoot2Application.class, args);
		
		String[] names = context.getBeanDefinitionNames();
		
		for(String name : names) {
			System.out.println(name);
		}
	}

}
