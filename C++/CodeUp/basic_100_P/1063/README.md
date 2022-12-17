
## 문제
#### 입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
#### 단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a>b ? a:b);
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
	cout << (a > b ? a : b) << endl;

	return 0;
}
```
