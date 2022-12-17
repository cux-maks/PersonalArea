
## 문제
#### 정수형(int)으로 변수를 선언하고, 변수에 정수값을 저장한 후
#### 변수에 저장되어 있는 값을 그대로 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);
	printf("%d", a);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int num;

	cin >> num;
	cout << num << endl;

	return 0;

}

```
