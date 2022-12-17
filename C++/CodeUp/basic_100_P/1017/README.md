
## 문제
#### int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);
	printf("%d %d %d", a, a, a);
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
	cout << num << " " << num << " " << num << endl;

	return 0;

}

```
