
## 문제
#### 정수가 순서대로 입력된다.
#### -2147483648 ~ +2147483647, 단 개수는 알 수 없다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
start:
	scanf("%d", &a);
	if (a != 0) {
		printf("%d\n", a);
		goto start;
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

re:

	cin >> a;

	if (a != 0) {
		cout << a << endl;
		goto re;
	}
	else {
		goto end;
	}

end:

	return 0;

}
```
