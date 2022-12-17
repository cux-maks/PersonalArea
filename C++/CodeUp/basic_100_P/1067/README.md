
## 문제
#### 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);
	if (a < 0) {
		printf("minus\n");
	}
	else {
		printf("plus\n");
	}
	if (a % 2 == 0) {
		printf("even\n");
	}
	else {
		printf("odd\n");
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

	string pm = a > 0 ? "plus" : "minus";
	string eo = a % 2 == 0 ? "even" : "odd";

	cout << pm << endl << eo << endl;

	return 0;

}
```
