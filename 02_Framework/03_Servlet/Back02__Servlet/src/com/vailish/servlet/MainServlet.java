package com.vailish.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.vailish.dto.Person;

@WebServlet("/Main")
public class MainServlet extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html; charset=UTF-8");
		
		doProcess(request, response);
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html; charset=UTF-8");
		doGet(request, response);
	}
	
	private void doProcess(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String action = request.getParameter("action");
		
		switch (action) {
		case "regist":
			doRegist(request, response);
			break;
		case "gugu":
			doGuGu(request, response);
			break;
		default:
			//아무것도 아닐때 처리
			break;
		}

}

	private void doGuGu(HttpServletRequest request, HttpServletResponse response) {
		int dan = Integer.parseInt(request.getParameter("dan"));
		
		PrintWriter writer = response.getWriter();
		
		writer.append("<html>");
		writer.append("<head>");
		writer.append("<title>구구단</title>");
		writer.append("</head>");
		writer.append("<body>");
		writer.append("<h1>구구단</h1>");
		for (int i = 1; i <= 9; i++) {
			writer.printf("%d * %d = %d<br>", dan, i, dan * i);
		}
		writer.append("</body>");
		writer.append("</html>");
	}

	private void doRegist(HttpServletRequest request, HttpServletResponse response) {
		String name = request.getParameter("name");
		int age = Integer.parseInt(request.getParameter("age"));
		String gender = request.getParameter("gender");
		String[] hobbies = request.getParameterValues("hobby");
		
//		System.out.println(request.getParameterValues("hobby"));
//		System.out.println(Arrays.toString(request.getParameterValues("hobby")));
		
		Person p = new Person(name, age, gender, hobbies);
		
		PrintWriter writer = response.getWriter();
		writer.append("<html>");
		writer.append("<head>");
		writer.append("<title>PersonInfo</title>");
		writer.append("</head>");
		writer.append("<body>");
		writer.append("<h1>등록한 사람 정보</h1>");
		writer.append(p.toString());
		writer.append("</body>");
		writer.append("</html>");
	}
