
## 문제
#### 정보 선생님은 오늘도 이상한 출석을 부른다.

#### 영일이는 오늘도 다른 생각을 해보았다.
#### 출석 번호를 다 부르지는 않은 것 같은데... 가장 빠른 번호가 뭐였지?

#### 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int num[10001] = {};
	int total;
	scanf("%d", &total);
	for (int i = 1; i <= total; i++) {
		scanf("%d", &num[i]);
		if (i != 1) {
			if (num[i] >= num[i - 1]) {
				num[i] = num[i - 1];
			}
		}
	}
	printf("%d", num[total]);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int n, a;
	int result = 23;

	cin >> n;

	for (int i = 0; i < n; i++) {

		cin >> a;
		result = result < a ? result : a;

	}

	cout << result;

	return 0;

}
```
