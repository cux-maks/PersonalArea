# JAVA

1001
```java
public class Main {
	
	public static void main(String[] args) {
		
		System.out.println("Hello");
		
	}
	
}
```

1002
```java
public class Main {
	
	public static void main(String[] args) {
		
		System.out.println("Hello World");
		
	}
	
}
```

1003
```java
public class Main {
	
	public static void main(String[] args) {
		
		System.out.println("Hello\nWorld");
		
	}
	
}
```

1004
```java
public class Main {
	
	public static void main(String[] args) {
		
		System.out.println("\'Hello\'");
		
	}
	
}
```

1005
```java
public class Main {
	
	public static void main(String[] args) {
		
		System.out.println("\"Hello World\"");
		
	}
	
}
```

1006
```java
public class Main {
	
	public static void main(String[] args) {
		
		System.out.println("\"!@#$%^&*()\"");
		
	}
	
}
```

1007
```java
public class Main {
	
	public static void main(String[] args) {
		
		System.out.println("\"C:\\Download\\hello.cpp\"");
		
	}
	
}
```

1008
```java
public class Main {
	
	public static void main(String[] args) {
		
		System.out.print('\u250C');
		System.out.print('\u252C');
		System.out.println('\u2510');
		System.out.print('\u251C');
		System.out.print('\u253C');
		System.out.println('\u2524');
		System.out.print('\u2514');
		System.out.print('\u2534');
		System.out.println('\u2518');
		
	}
	
}
```

1010
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		System.out.println(num);
		
		
	}
	
}
```

1011
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		char c = sc.next().charAt(0);
		
		System.out.println(c);
		
		
	}
	
}
```

1012
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		float c = sc.nextFloat();
		
		System.out.println(String.format("%.6f", c));
		
		
	}
	
}
```

1013
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d %d", a, b);
		
		
	}
	
}
```

1014
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		char a = sc.next().charAt(0);
		char b = sc.next().charAt(0);
		
		sc.close();
		
		System.out.printf("%c %c", b, a);
		
		
	}
	
}
```

1015
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		float a = sc.nextFloat();
		
		System.out.printf("%.2f", a);
		
		
	}
	
}
```

1017
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		
		System.out.printf("%d %d %d", a, a, a);
		
		
	}
	
}
```

1018
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String a = sc.nextLine();
		
		System.out.printf(a);
		
		
	}
	
}
```

1019
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.next();
		String[] arr = str.split("\\.");
		
		int y = Integer.valueOf(arr[0]);
		int m = Integer.valueOf(arr[1]);
		int d = Integer.valueOf(arr[2]);
		
		System.out.printf("%04d.%02d.%02d", y, m, d);
		
	}
	
}
```

1020
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.next();
		String[] arr = str.split("\\-");
		
		System.out.printf("%s%s", arr[0], arr[1]);
		
	}
	
}
```

1021
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.next();
		
		System.out.printf("%s", str);
		
	}
	
}
```

1022
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String str = sc.nextLine();
		
		System.out.printf("%s", str);
		
	}
	
}
```

1023
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.next();
		String[] arr = str.split("\\.");
		
		System.out.printf("%s\n%s", arr[0], arr[1]);
		
	}
	
}
```

1024
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine();
		String[] arr = str.split("");
		
		for(int i = 0; i < arr.length; i++) {
			System.out.printf("\'%s\'\n", arr[i]);
		}
		
	}
	
}
```

1025
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine();
		String[] arr = str.split("");
		
		for(int i = 0; i < arr.length; i++) {
			System.out.printf("[%s", arr[i]);
			for(int j = 0; j < arr.length - 1 - i; j++) {
				System.out.printf("0");
			}
			System.out.printf("]\n");
		}
		
	}
	
}
```

1026
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine();
		String[] arr = str.split(":");
		
		System.out.printf("%d", Integer.parseInt(arr[1]));
		
	}
	
}
```

1027
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine();
		String[] arr = str.split("\\.");
		
		System.out.printf("%s-%s-%s", arr[2], arr[1], arr[0]);
		
	}
	
}
```

1028
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long num = sc.nextLong();
		
		System.out.printf("%d", num);		
	}
	
}
```

1029
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		double num = sc.nextDouble();
		
		System.out.printf("%.11f", num);		
	}
	
}
```

1030
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String num = sc.nextLine();
		
		System.out.printf("%s", num);		
	}
	
}
```

1031
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		System.out.printf("%o", num);		
	}
	
}
```

1032
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		System.out.printf("%x", num);		
	}
	
}
```

1033
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		System.out.printf("%X", num);		
	}
	
}
```

1034
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String num = sc.next();
		int result = Integer.parseInt(num, 8);
		
		System.out.printf("%d", result);		
	}
	
}
```

1035
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String num = sc.next();
		int result = Integer.parseInt(num, 16);
		
		System.out.printf("%o", result);		
	}
	
}
```

1036
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		char num = sc.next().charAt(0);
		
		System.out.printf("%d", (int)num);		
	}
	
}
```

1037
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		System.out.printf("%c", (char)num);		
	}
	
}
```

1038
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		long b = sc.nextLong();
		
		System.out.printf("%d", a + b);		
	}
	
}
```

1039
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		long b = sc.nextLong();
		
		System.out.printf("%d", a + b);		
	}
	
}
```

1040
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		
		System.out.printf("%d", -a);		
	}
	
}
```

1041
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		char a = sc.next().charAt(0);
		
		System.out.printf("%c", a + 1);		
	}
	
}
```

1042
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d", a / b);		
	}
	
}
```

1043
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d", a % b);		
	}
	
}
```

1044
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		
		System.out.printf("%d", a + 1);		
	}
	
}
```

1045
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		long b = sc.nextLong();
		
		System.out.printf("%d\n", a + b);
		System.out.printf("%d\n", a - b);
		System.out.printf("%d\n", a * b);
		System.out.printf("%d\n", a / b);
		System.out.printf("%d\n", a % b);
		System.out.printf("%.2f\n", (float)a / (float)b);
	}
	
}
```

1046
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		long b = sc.nextLong();
		long c = sc.nextLong();
		
		System.out.printf("%d\n", a + b + c);
		System.out.printf("%.1f", (float)(a+b+c) / 3.0);
	
	}
}
```

1047
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		
		System.out.printf("%d\n", a<<1);
	
	}
}
```

1048
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		long b = sc.nextLong();
		
		System.out.printf("%d\n", a * (1 << b));
	
	}
}
```

1049
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		long b = sc.nextLong();
		
		System.out.printf("%d\n", a > b ? 1 : 0);
	
	}
}
```

1050
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		long b = sc.nextLong();
		
		System.out.printf("%d\n", a == b ? 1 : 0);
	
	}
}
```

1051
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		long b = sc.nextLong();
		
		System.out.printf("%d\n", a <= b ? 1 : 0);
	
	}
}
```

1052
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		long b = sc.nextLong();
		
		System.out.printf("%d\n", a != b ? 1 : 0);
	
	}
}
```

1053
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		
		System.out.printf("%d\n", a == 1 ? 0 : 1);
	
	}
}
```

1054
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d\n", (a == 1)&&(b == 1) ? 1 : 0);
	
	}
}
```

1055
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d\n", (a == 1)||(b == 1) ? 1 : 0);
	
	}
}
```

1056
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d\n", a != b ? 1 : 0);
	
	}
}
```

1057
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d\n", a == b ? 1 : 0);
	
	}
}
```

1058
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d\n", (a == 0) && (b == 0) ? 1 : 0);
	
	}
}
```

1059
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		// int b = sc.nextInt();
		
		System.out.printf("%d\n", ~a);
	
	}
}
```

1060
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d\n", a & b);
	
	}
}
```

1061
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d\n", a | b);
	
	}
}
```

1062
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d\n", a ^ b);
	
	}
}
```

1063
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.printf("%d\n", a > b ? a : b);
	
	}
}
```

1064
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		
		System.out.printf("%d\n", (a < b ? a : b) < c ? (a < b ? a : b) : c);
	
	}
}
```

1065
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		
		if(a % 2 == 0) {
			System.out.println(a);
		}
		if(b % 2 == 0) {
			System.out.println(b);
		}
		if(c % 2 == 0) {
			System.out.println(c);
		}
	}
}
```

1066
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		
		if(a % 2 == 0) {
			System.out.println("even");
		}else {
			System.out.println("odd");
		}
		if(b % 2 == 0) {
			System.out.println("even");
		}else {
			System.out.println("odd");
		}
		if(c % 2 == 0) {
			System.out.println("even");
		}else {
			System.out.println("odd");
		}
	}
}
```

1067
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		// int b = sc.nextInt();
		// int c = sc.nextInt();
		
		if(a > 0) {
			System.out.println("plus");
		}else {
			System.out.println("minus");
		}
		
		if(a % 2 == 0) {
			System.out.println("even");
		}else {
			System.out.println("odd");
		}
		
	}
}
```

1068
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		
		if(a >= 90 && a <= 100) {
			System.out.println("A");
		}else if(a >= 70 && a <= 89) {
			System.out.println("B");
		}else if(a >= 40 && a <= 69) {
			System.out.println("C");
		}else if(a >= 0 && a <= 39) {
			System.out.println("D");
		}
	}
}
```

1069
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String result = sc.next();
		
		if(result.equals("A")) {
			System.out.println("best!!!");
		}else if(result.equals("B")) {
			System.out.println("good!!");
		}else if(result.equals("C")) {
			System.out.println("run!");
		}else if(result.equals("D")) {
			System.out.println("slowly~");
		}else {
			System.out.println("what?");
		}
	}
}
```

1070
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int month = sc.nextInt();
	
		switch(month) {
		case 12:
		case 1:
		case 2:
			System.out.println("winter");
			break;
		case 3:
		case 4:
		case 5:
			System.out.println("spring");
			break;
		case 6:
		case 7:
		case 8:
			System.out.println("summer");
			break;
		case 9:
		case 10:
		case 11:
			System.out.println("fall");
			break;
		}
	}
}
```

1071
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		while(true) {
			
			int a = sc.nextInt();
			
			if(a != 0) {
				System.out.println(a);
			}else {
				break;
			}
			
		}
	}
}
```

1072
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		long n = sc.nextLong();
		
		for(long i = 0; i < n; i++) {
			int a = sc.nextInt();
			System.out.println(a);
		}
	}
}
```

1073
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		while(true) {
			
			int a = sc.nextInt();
			
			if(a != 0) {
				System.out.println(a);
			}else {
				break;
			}
			
		}
	}
}
```

1074
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int a = sc.nextInt();
		
		for(int i = a; i > 0; i--) {
			System.out.println(i);
		}
	}
}
```

1075
```java
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int a = sc.nextInt();
		
		for(int i = a - 1; i >= 0; i--) {
			System.out.println(i);
		}
	}
}
```
