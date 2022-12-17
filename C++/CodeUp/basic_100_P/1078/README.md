
## 문제
#### 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a, n, val;
	scanf("%d", &a);
	n = a / 2;
	val = (n * n) + n;
	printf("%d", val);

	return 0;
}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int a;
	int result = 0;

	cin >> a;

	for (int i = 0; i <= a; i++) {

		result = i % 2 == 0 ? result + i : result;

	}

	cout << result << endl;

	return 0;

}
```
