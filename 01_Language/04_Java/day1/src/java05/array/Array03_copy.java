package java05.array;

import java.util.Arrays;

public class Array03_copy {
	public static void main(String[] args) {
		
		int[] arr = {77, 50, 10, 12, 64, 15};

		int[] tmp = new int[arr.length*2];
		//arraycopy 사용하기
		
		int[] tmp2 = new int[arr.length*2];
		
		System.arraycopy(arr, 0, tmp2, 0, arr.length);
		// System.arraycopy(src, srcPos, dest, destPos, length);
		// (복사할 배열, , 붙여넣기할 배열, 붙여넣기 시작점, 복사한 배열 끝 요소)
		// Object src: 복사하고자 하는 소스
		// int srcPos : 원본 소스에서 어느 부분부터 읽어올지 위치 정하기(0이면 처음부터)
		// Oject dest : 복사할 소스(복사하려는 대상)
		// int destPos : 위의 복사본에서 자료를 받을 때, 어느 부분부터 쓸 것인지 시작위치(0이면 처음부터)
		// int length : 원본에서 복사본으로 데이터를 읽어서 쓸 데이터 길이(원본에서 복사본까지 얼만큼 읽어올지 입력)
		

		
		System.out.println(Arrays.toString(tmp2));
		// 반복문을 이용해서 복사하기
		
		int[] arr2 = {1, 3, 5, 7, 9};
		
		int[] temp = new int[arr2.length*2];
		
		for(int i = 0; i<arr2.length; i++) {
			temp[i] = arr2[i];
		}
		System.out.println(Arrays.toString(temp));
	}
}
