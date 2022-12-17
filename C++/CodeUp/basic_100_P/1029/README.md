
## 문제
#### 실수 1개를 입력받아 그대로 출력해보자.
#### (단, 입력되는 실수의 범위는 +- 1.7\*10^-308 ~ +- 1.7\*10^308 이다.)

###### \<c\>
```c
#include <stdio.h>

int main() {

	double a;
	scanf("%lf", &a);
	printf("%.11lf", a);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	double d;

	cin >> d;

	cout << fixed;
	cout.precision(11);
	cout << d << endl;

	return 0;

}
```
