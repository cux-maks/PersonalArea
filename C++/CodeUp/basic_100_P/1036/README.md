
## 문제
#### 영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	char a;
	scanf("%c", &a);
	printf("%d", a);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	char n;

	cin >>  n;
	cout << int(n) << endl;

	return 0;

}
```
