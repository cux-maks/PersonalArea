
## 문제
#### n개의 정수가 순서대로 입력된다.
#### -2147483648 ~ +2147483647, 단 n의 최대 개수는 알 수 없다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int num, a;
	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		scanf("%d", &a);
		printf("%d\n", a);
	}

	return 0;
}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int n, a;

	cin >> n;

re:

	cin >> a;
	if (n-- != 0) {

		cout << a << endl;
		goto re;

	}
	else {

		goto end;

	}

end:

	return 0;

}
```
