# Spring MVC - 요청 처리 흐름
1. 클라이언트 요청이 들어오면 DispatcherServlet이 받음
2. HandlerMapping이 어떤 Controller가 요청을 처리할 지 결정
3. DispatcherServlet은 Controller에 요청을 전달
4. Controller는 요청을 처리
5. 결과(요청처리를 위한 data, 결과를 보여줄 view의 이름)를 ModelAndView에 담아 반환
6. ViewResolver에 의해서 실제 결과를 처리할 View를 결정하고 반환
7. 결과를 처리할 View에 ModelAndView를 전달
8. DispatcherServlet은 View가 만들어낸 결과를 응답