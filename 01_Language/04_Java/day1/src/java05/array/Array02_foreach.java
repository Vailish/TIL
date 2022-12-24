package java05.array;

import java.util.Arrays;

public class Array02_foreach {
	public static void main(String[] args) {
		
//		long l = 3000000000L;
//		long l = 3000000000;  // 이거는 안됨, 기본 int형이기 때문에 L을 써서 롱임을 알려야 함
		
		
		int[] arr = {77, 50, 10, 12, 64, 15};
		
		for(int x : arr) { // 이렇게 해도 복사해서 가져오는거라 원본은 안 변함
			x *= 2;
		}
		
		
		for(int i = 0; i<arr.length; i++) { // 그래서 for 문을 써서 이렇게 해주면 됨
			arr[i] *= 2;
		}
		
		for(int x : arr) {
			System.out.println(x);
		}
		
		System.out.println(Arrays.toString(arr)); // 파이썬 리스트 출력과 동일한 형식으로 출력해줌
	}
}
