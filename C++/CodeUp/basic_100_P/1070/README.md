
## 문제
#### 월이 입력될 때 계절 이름이 출력되도록 해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);

	switch (a) {
	case 12:
	case 1:
	case 2:
		printf("winter");
		break;
	case 3:
	case 4:
	case 5:
		printf("spring");
		break;
	case 6:
	case 7:
	case 8:
		printf("summer");
		break;
	case 9:
	case 10:
	case 11:
		printf("fall");
		break;
	}

	return 0;
}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int month;
	string season;

	cin >> month;

	season = month == 12 || month == 1 || month == 2 ? "winter" : "other";
	season = month == 3 || month == 4 || month == 5 ? "spring" : season;
	season = month == 6 || month == 7 || month == 8 ? "summer" : season;
	season = month == 9 || month == 10 || month == 11 ? "fall" : season;

	cout << season << endl;

	return 0;

}
```
