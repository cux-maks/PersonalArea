
## 문제
#### 영문자 1개를 입력받아 그 다음 문자를 출력해보자.

#### 영문자 'A'의 다음 문자는 'B'이고, 영문자 '0'의 다음 문자는 '1'이다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	char a;
	scanf("%c", &a);
	printf("%c", a+1);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	char s;

	cin >> s;
	cout << char(s + 1) << endl;

	return 0;

}
```
