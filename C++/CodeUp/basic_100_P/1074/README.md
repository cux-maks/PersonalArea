
## 문제
#### 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);
	for (int i = a; i > 0; i--) {
		printf("%d\n", i);
	}

	return 0;
}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int a;

	cin >> a;

	while (true) {
		
		cout << a << endl;
		a--;

		if (a == 0) {
			break;
		}

	}

	return 0;

}
```
