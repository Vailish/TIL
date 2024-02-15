# Java 기본 문법

- 배열
- 다차원 배열


# 배열(Array)
- 같은 종류의 데이터를 저장하기 위한 자료구조
  - 파이썬의 list와는 조금 다르다고 할 수 있음, 머든 다 넣을 수 있으니까
  - cf) Arraylist의 경우는 어느정도 차면 알아서 더 큰 녀석을 만들어서 옮겨줌
- 크기가 고정(한 번 생성된 배열은 크기를 바꿀 수 없음)
- 배열을 객체로 취급(참조, String 방식)
- 배열의 요소를 참조하려면 배열이름과 색인(index)이라고 하는 int 유형의 정수 값을 조합하여 사용
- JVM
  - stack : 기본형 값 저장, string & 배열과 같은 참조형의 주소정보(배열의 첫번째 값의 주소)가 저장됨
  - heap : String, 배열 값 저장
  - 그래서 new String('서울')처럼 만들 수 있음, 이때의 값은 기존 '서울'값이 아닌 새로운 주소값이기 때문에 비교하면 다르게나옴
  - stack에는 이름과 주소, heap에서는 가리키는 녀석의 값을 저장한다고 생각하면됨. 다만 이미 같은 값이 heap에 존재하고 있으면 그 녀석의 주소를 stack에 저장을 하고, new를 사용하면 그 녀석이 있든 없든 간에 heap영역에 새로 만들고 그 녀석의 주소를 stack 이름에 저장함

## 배열의 선언
- `타입[ ] 변수`, 위 방식으로하자 헷갈리니까 통일
- 타입 변수[ ]

|타입|배열이름|선언|
|------|---|---|
|int|iArr|int[] iArr;|
|char|cArr|char[] cArr;|
|boolean|bArr|boolean[] bArr;|
|String|strArr|String[] strArr;|
|Date|dateArr|Date[] dateArr;|

## 배열의 생성과 초기화
- 자료형[] 배열이름 = {값1, 값2, 값3, 값4};
  - 선언과 동시에 초기화
- 배열이름 = new 자료형[] {값1, 값2, 값3, 값4};
  - 배열 생성 및 값 초기화
- 배열이름 = new 자료형[길이];
  - 배열 생성(자료형의 초기값으로 초기화)

|자료형|기본값|비고|
|------|---|---|
|boolean|false||
|char|'\|u0000'(\|=원 기호)|공백문자|
|byte, short, int|0||
|long|0L||
|float|0.0f||
|double|0.0||
|참조형 변수|null|아무것도 참조하지 않음|

## 배열의 사용
- index 번호를 가지고 각 요소에 접근
- index 번호는 0부터 시작
- 배열이름`.length`를 통해 `배열의 길`이 조회 가능
  - 객체취급이기 때문
- 배열의 길이는 임의로 변경 불가 따라서 더 큰 배열을 생성 후 내용을 옮김
- 이렇게 옮기고 나면 기존에 썻던 녀석은 아무대서도 참조를 하지 않기 때문에 해당 녀석을 GC(garbage collector)가 자동으로 없애고 메모리 확보
  - 자바의 메모리는 사용자가 관리하지 않고 GC라는 녀석이 처리함. GC를 직접 불러올 수는 있지만, 권장되지않음
![image](https://user-images.githubusercontent.com/109258380/209283731-bb097f9b-a04e-4a6b-a85b-6031d521bfc5.png)

# for-each
- 가독성이 개선된 반복문으로, 배열 및 collections 에서 사용
- index 대신 직접 요소(elements)에 접근하는 변수를 제공
- naturally read only (copied value)
```java
int intArray [] = {1, 3, 5, 7, 9};
for(int x : intArray){
  System.out.println(x);
}

for(int i=0; i<intArray.length; i++){
  int x = intArray[i];
  System.out.println(x);
}
```

## 배열의 출력
- 반복문을 통해서 출력
- Arrays.toString(배열) : 배열 안의 요소를 [값1, 값2, ...] 형태로 출력

## 배열의 복사
- 배열은 생성하면 길이를 변경할 수 없기 떄문에 더 많은 저장공간이 필요하다면 큰 배열을 생성하고 이전 배열의 값을 복사해야함

## 배열의 복사
- System.arraycopy(Oject src, int srcPos, Object dest, int desPos, int length)
- src : 원본배열
- srcPos : 원본배열 복사 시작 위치
- dest : 복사할 배열
- destPos : 복사 받을 시작 위치
- length : 복사할 크기
```java
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
```

## 배열 실습 문제
1. 최대값, 최소값 찾기

```java
// solution 1
int[] intArray = {3, 27, 13, 8, 235, 7, 22, 9, 435, 31, 54};

int min = 1000;
int max = 0;
for(int num: intArray){
  if(num>max) {
    max = num;
  }
  if(num<min) {
    min = num;
  }
}
System.out.printf("min: %d, max: %d%n", min, max);

// solution 2
int[] intArray = {3, 27, 13, 8, 235, 7, 22, 9, 435, 31, 54};

int min = Integer.MAX_VALUE;
int max = Integer.MIN_VALUE;

for (int num : intArray) {
  min = Math.min(min, num);
  max = Math.max(max, min);
}

System.out.printf("min: %d, max: %d%n", min, max);
```

2. 빈도수 구하기
```java
int[] intArray = {3, 7, 2, 5, 7, 7, 9, 2, 8, 1, 1, 5, 3};

int[] used = new int[10];

for(int num:intArray) {
  used[num]++;
}
System.out.println(Arrays.toString(used));
```

# 다차원 배열

## 다차원 배열(Multidimensional Array)이란?
- 2차원 이상의 배열을 의미
- 배열 요소로 또 다른 배열을 가지는 배열
- 2차원 배열은 배열 요소로 1차원 배열의 참조를 가지는 배열
- 3차원 배열은 배열 요소로 2차원 배열의 참조를 가지는 배열

## 2차원 배열 선언
```java
int[][] iArr
int iArr[][]
int[] iArr[]
```

## 2차원 배열 생성
```java
배열의 이름 = new 배열유형[1차원 배열개수][1차원 배열의 크기];
// 
배열의 이름 = new 배열유형[1차원 배열개수][];
```

## 2차원 배열
![image](https://user-images.githubusercontent.com/109258380/209286210-9f5c92da-8be3-4ef6-92ec-b87a895e5bb7.png)
![image](https://user-images.githubusercontent.com/109258380/209286709-2ccae188-3243-4f9a-b3dd-405b7ccf5659.png)
- 2차원배열 = 1차원 배열들의 배열
  - 1차원 배열들은 모두 크기(길이)가 같아야 하지 않음, 달라도 됨

## 2차원 배열 메모리
```java
int a = 10;

int [] arr = new int[4];

int [][] arr2 = new int[2][];
arr2[0] = new int [3];
arr2[1] = new int [3];
arr2[1][1] = 100;
```

## 2차원 배열 탐색
- 모든 2차원 배열의 원소 중 3의 배수의 개수와 그들의 합을 출력
- 델타 이동
```java
public static void main(String[] args) {
  int[][] grid = {
    {2, 3, 1, 4, 7},
    {8, 13, 3, 33, 1},
    {7, 4, 5, 80, 12},
    {17, 9, 11, 5, 4},
    {4, 5, 91, 27, 7}
  }
 int count = 0;
 int sum = 0;
 for(int [] row: grid) {
  for(int num:row) {
    if(num%3==0) {
      count++;
      sum += num;
    }
  }
 }
 System.out.printf("개수: %d, 총합: %d%n", count, sum);
}
 
```
