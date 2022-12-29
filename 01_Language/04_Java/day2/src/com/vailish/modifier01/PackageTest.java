package com.vailish.modifier01;

//import java.lang.*;  //자동으로 들어있어서 그냥 system.out.println 등을 쓸 수 있는것

import java.util.Arrays;
import java.util.Scanner;  //package아래에사용 , 이름 전체를 풀패키지명이라고함
//import java.util.*;
import java.util.function.Function;

import class03.Person;
import class04.DogTest;
// 이거 주석으로하고 위의 *를 살려도 작동안함(하위는 포함안됨, 동레벨만)
// ctrl shift o 하면 알아서 import해줌

public class PackageTest {
	public static void main(String[] args) {
		Scanner sc;
		
		Arrays arr;
		
		Function f;
		
		Person p;  // class03에 있는 Person 이라는 것을 가지고옴

		class02.Person p2; // 굳이 02에 Person을 들고오려면 이렇게 하면됨
		
//		DogTest dt;
	}
}
