package tobyspring.helloboot;

public class SimpleHelloSerivce implements HelloService {
	@Override
	public String sayHello(String name) {
		return "Hello " + name;
	}
}
