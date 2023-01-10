package com.ssafy.board.controller;

import java.io.IOException;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.ssafy.board.model.dao.BoardDao;
import com.ssafy.board.model.dao.BoardDaoImpl;
import com.ssafy.board.model.dto.Board;

import sun.awt.RepaintArea;

@WebServlet("/board")
public class BoardController extends HttpServlet {

	private BoardDao dao = BoardDaoImpl.getInstance();

	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// GET 요청에서는 딱히 안해도 되지만 POST 요청이 들어왔을때
		if (request.getMethod().equals("POST"))
			request.setCharacterEncoding("UTF-8");

		// Front-Controller 패턴
		String act = request.getParameter("act");

		switch (act) {
		case "list":
			doList(request, response);
			break;
		case "writeform":
			doWriteForm(request, response);
			break;
		case "write":
			doWrite(request, response);
			break;
		case "detail":
			doDetail(request, response);
			break;
		case "updateform":
			doUpdateform(request, response);
			break;
		case "update":
			doUpdate(request, response);
			break;
		case "delete":
			doRemove(request, response);
			break;
		default:
			break;
		}
	}

	private void doRemove(HttpServletRequest request, HttpServletResponse response) throws IOException {
		int id = Integer.parseInt(request.getParameter("id"));
		try {
			dao.deleteBoard(id);
			response.sendRedirect("board?act=list");
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

	private void doUpdate(HttpServletRequest request, HttpServletResponse response) throws IOException {
		try {
//			Board board = dao.selectOne(Integer.parseInt(request.getParameter("id")));
			Board board = new Board();
			board.setId(Integer.parseInt(request.getParameter("id")));
			board.setTitle(request.getParameter("title"));
			board.setContent(request.getParameter("content"));
			board.setWriter(request.getParameter("writer")); //이경우엔 세팅해줘야함
			
			dao.updateBoard(board);
			response.sendRedirect("board?act=list");
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private void doUpdateform(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		int id = Integer.parseInt(request.getParameter("id"));
		try {
			Board board = dao.selectOne(id);
			request.setAttribute("board", board);
			request.getRequestDispatcher("/board/updateform.jsp").forward(request, response);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	private void doDetail(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		int id = Integer.parseInt(request.getParameter("id"));

		try {
			dao.updateViewCnt(id);
			request.setAttribute("board", dao.selectOne(id));
			request.getRequestDispatcher("/board/detail.jsp").forward(request, response);
		} catch (SQLException e) {
			e.printStackTrace();
		}

	}

	private void doWrite(HttpServletRequest request, HttpServletResponse response) throws IOException {
		Board board = new Board();

		board.setTitle(request.getParameter("title"));
		board.setWriter(request.getParameter("writer"));
		board.setContent(request.getParameter("content"));

		try {
			dao.insertBoard(board);
		} catch (SQLException e) {
			e.printStackTrace();
		}

		response.sendRedirect("board?act=list");
	}

	private void doWriteForm(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.getRequestDispatcher("/board/writeform.jsp").forward(request, response);
	}

	private void doList(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// list 라고 하는 이름으로 전체 게시글 리스트를 가져와 request 영역에 저장하겠다.
		request.setAttribute("list", dao.selectAll());
		request.getRequestDispatcher("/board/list.jsp").forward(request, response);
	}

}
