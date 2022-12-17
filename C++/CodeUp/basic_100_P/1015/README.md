
## 문제
#### 실수(float) 1개를 입력받아 저장한 후,
#### 저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여
#### 소수점 이하 둘 째 자리까지 출력하시오.

###### \<c\>
```c
#include <stdio.h>

int main() {

	float a;
	scanf("%f", &a);
	printf("%.2f", a);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	float num;

	cin >> num;
	cout << fixed;
	cout.precision(2);
	cout << num << endl;

	return 0;

}

```
