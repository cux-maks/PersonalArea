
## 문제
#### 10진수를 입력받아 8진수(octal)로 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);
	printf("%o", a);
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
	cout << oct << n << endl;

	return 0;

}
```
