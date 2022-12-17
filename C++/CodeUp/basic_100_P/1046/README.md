
## 문제
#### 정수 3개를 입력받아 합과 평균을 출력해보자.
#### 단, -2147483648 ~ +2147483647

###### \<c\>
```c
#include <stdio.h>

int main() {

	long long int a, b, c;
	scanf("%lld %lld %lld", &a, &b, &c);
	printf("%lld\n%.1f", a+b+c, (float)(a+b+c)/3);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>>

using namespace std;

int main() {

	long long int a, b, c;

	cin >> a >> b >> c;

	cout << a + b + c << endl;
	cout.precision(1);
	cout << fixed << (float(a) + float(b) + float(c)) / 3 << endl;

	return 0;

}
```
