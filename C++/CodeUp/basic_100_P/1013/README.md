1013
## 문제
#### 정수(int) 2개를 입력받아 그대로 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d %d", a, b);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int a, b;

	cin >> a >> b;
	cout << a << " " << b << endl;

	return 0;

}

```
