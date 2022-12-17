
## 문제
#### 두 정수(a, b)를 입력받아
#### b가 a보다 크거나 같으면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.


###### \<c\>
```c
#include <stdio.h>

int main() {

	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a <= b);
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
	
	if (b >= a) {
		cout << 1 << endl;
	}
	else {
		cout << 0 << endl;
	}

	return 0;

}
```
