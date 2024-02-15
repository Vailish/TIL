# Map

## Map
- 생성방식
  - Map<String, String> map = new HashMap<>(); 
  - HashMap<String, Object> map2 = new HashMap<>();
  - Map<Key, Value>라고 생각하면 됨
  - Map은 순서가 없음
```java
	Map<String, Object> map = new HashMap<String, Object>();

		map.put("name", "vailish");
		map.put("age", 20);
		map.put("hobby", "coding");
        map.put("age", 25);

		System.out.println(map.keySet()); // [name, age, hobby]
		System.out.println(map.values()); // [vailish, 25, coding]
		System.out.println(map.toString()); // {name=vailish, age=25, hobby=coding}
```

## HashMap vs LinkedHashMap
||HashMap|LinkedHashMap|
|:---:|:---:|:---:|
|순서|X|O|

### Spring에서의 Model vs ModelMap
- 공통점 : Map 인터페이스 사용
- 차이점 : ModelMap 은 LinkedHashMap을 상속받고, Model은 Map을 상속 받음(보다 자유로움)

