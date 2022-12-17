
## 문제
#### 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	char a;
start:
	scanf("%c ", &a);
	if (a != 'q') {
		printf("%c\n", a);
		goto start;
	}
	else {
		printf("q\n");
	}


	return 0;
}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	char a;

	while (true) {

		cin >> a;

		if (a != 'q') {
			cout << a << endl;
		}
		else {
			cout << a << endl;
			break;
		}

	}

	return 0;

}
```
