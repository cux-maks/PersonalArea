
## 문제
#### 어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int h, m;
	scanf("%d:%d", &h, &m);
	printf("%d:%d", h, m);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main(void) {

	int a, b;
	char x;

	cin >> a >> x >> b;

	cout << a << x << b;

	return 0;

}

```
