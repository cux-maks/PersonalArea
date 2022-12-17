
## 문제
#### 2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	char a, b;
	scanf("%c %c", &a, &b);
	printf("%c %c", b, a);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	char x, y;

	cin >> x >> y;
	cout << y << " " << x << endl;

	return 0;

}
```
