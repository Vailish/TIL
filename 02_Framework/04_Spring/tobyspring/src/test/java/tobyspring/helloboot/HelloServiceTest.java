package tobyspring.helloboot;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;

public class HelloServiceTest {
	@Test
	void simpleHelloService() {
		SimpleHelloSerivce helloService = new SimpleHelloSerivce();
		
		String ret = helloService.sayHello("Test");
		
		Assertions.assertThat(ret).isEqualTo("Hello Test");
	}
}
