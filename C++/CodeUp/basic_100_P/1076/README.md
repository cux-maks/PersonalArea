
## 문제
#### 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	char a;
	scanf("%c", &a);
	for (int i = 97; i <= (int)a; i++) {
		printf("%c ", i);
	}

	return 0;
}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	char a;

	cin >> a;

	for (int i = 97; i < int(a); i++) {
		cout << char(i) << " ";
	}

	cout << char(a) << endl;

	return 0;
}
```
