package java04.control;

public class SwitchTest {
	public static void main(String[] args) {
		
		//달을 확인해 해당 달이 31일 인지, 30일 인지 확인, 2월은 예외
		
		int month = 12;
		
		switch(month) {
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:
			System.out.println("31일");
			break;
		case 4:
		case 6:
		case 9:
		case 11:
			System.out.println("30일");
		case 2:
			// 윤년인지 아닌지 판단해야함.
			System.out.println("28일");
			break;
		default:
			System.out.println("그러한 달은 없음");
			break;
		}
	}
}
