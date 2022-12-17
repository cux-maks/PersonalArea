
## 문제
#### 온라인 채점시스템에는 초등학생, 중고등학생, 대학생, 대학원생,
#### 일반인, 군인, 프로그래머, 탑코더 등 아주 많은 사람들이 들어와 문제를 풀고 있는데,

#### 실시간 채점 정보는 메뉴의 채점기록(Judge Status)을 통해 살펴볼 수 있다.

#### 자! 여기서...잠깐..
#### 같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가
#### 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?


###### \<c\>
```c
#include <stdio.h>

int main() {

	int a, b, c, i=1;
	scanf("%d %d %d", &a, &b, &c);
	while (1) {
		if (i % a == 0 && i % b == 0 && i % c == 0) {
			printf("%d", i);
			break;
		}
		i++;
	}
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int a, b, c;
	int i = 0;
	bool k = 0;

	cin >> a >> b >> c;

	while (!k) {

		i++;
		k = i % a == 0 && i % b == 0 && i % c == 0 ? 1 : 0;

	}

	cout << i;

	return 0;

}
```
