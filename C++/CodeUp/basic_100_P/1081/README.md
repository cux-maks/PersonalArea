
## 문제
#### 1부터 n까지, 1부터 m까지 숫자가 적힌
#### 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a, b;
	scanf("%d %d", &a, &b);
	for (int i = 1; i <= a; i++) {
		for (int j = 1; j <= b; j++) {
			printf("%d %d\n", i, j);
		}
	}
	return 0;
}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int n, m;

	cin >> n >> m;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cout << i << " " << j << endl;
		}
	}

	return 0;

}
```
