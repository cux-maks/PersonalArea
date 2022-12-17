
## 문제
#### 10진 정수 1개를 입력받아 아스키 문자로 출력해보자.
#### 단, 0 ~ 255 범위의 정수만 입력된다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);
	printf("%c", a);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int n;

	cin >> n;
	cout << char(n) << endl;

	return 0;

}
```
