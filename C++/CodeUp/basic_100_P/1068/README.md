
## 문제
#### 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);
	if (a > 89) {
		printf("A");
	}else if (a > 69 && a < 90) {
		printf("B");
	}else if (a > 39 && a < 70) {
		printf("C");
	}else if (a < 40) {
		printf("D");
	}
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int score;

	cin >> score;

	if (score <= 100 && score >= 90) {
		cout << "A" << endl;
	}
	else if (score <= 89 && score >= 70) {
		cout << "B" << endl;
	}
	else if (score <= 69 && score >= 40) {
		cout << "C" << endl;
	}
	else if (score <= 39 && score >= 0) {
		cout << "D" << endl;
	}

	return 0;

}
```
