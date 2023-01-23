package tobyspring.helloboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import tobyspring.config.MySpringBootApplication;

@MySpringBootApplication
public class TobyspringApplication {

	public static void main(String[] args) {
		SpringApplication.run(TobyspringApplication.class, args);
	}

}
