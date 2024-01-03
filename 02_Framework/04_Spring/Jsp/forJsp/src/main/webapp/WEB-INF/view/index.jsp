<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <title>Document</title>
</head>
<body>
    jsp success!
<%!
   private int num1 = 0;
   public void jspInit() {
       System.out.println("owo");
   }
   public void jspDestory(){
       System.out.println("jspDestory실행됨");
   }
%>
<%
    int num2 = 0;
    num1 ++;
    num2 ++;
%>
<ul>
    <li>num1: <%= num1 %></li>
    <li>num2: <%= num2 %></li>
</ul>
<p>
    한글오류 멈춰!
    <link href="second.jsp">이동!
    </p>
</body>
</html>