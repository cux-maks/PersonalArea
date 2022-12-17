
## 문제
#### 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);
	for (int i = 0; i <= a; i++) {
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
	int i = 0;

	cin >> a;

	do {

		cout << i << endl;
		i++;

	} while (i != a + 1);

	return 0;
}
```
