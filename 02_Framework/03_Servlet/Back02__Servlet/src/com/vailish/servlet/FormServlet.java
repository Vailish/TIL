package com.vailish.servlet;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/FormServlet")
public class FormServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("GET");
		System.out.println(request.getParameter("name"));
		System.out.println(request.getParameter("age"));
		System.out.println(request.getParameter("gender"));
		
		String name = request.getParameter("name");
		//1. JS이용해ㅏ여 애초에 값을 안넣으면 여기까지 오지 못하게 막던가
		//2. if 같은거나 기타 등등의 방법을 활용하여 자바에서 컨트롤을 하던가
		int age = Integer.parseInt(request.getParameter("age"));
		String gender = request.getParameter("gender");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		System.out.println("POST");
		
		String name = request.getParameter("name");
		int age = Integer.parseInt(request.getParameter("age"));
		String gender = request.getParameter("gender");
		
		System.out.println(request.getParameter("name"));
		System.out.println(request.getParameter("age"));
		System.out.println(request.getParameter("gender"));
	}

}
