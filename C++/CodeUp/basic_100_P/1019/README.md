1019
## 문제
#### 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int y, m, d;
	scanf("%d.%d.%d", &y, &m, &d);
	printf("%04d.%02d.%02d", y, m, d);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>
#include <string>

using namespace std;

int main() {

	int y, m, d;
	char dot_1, dot_2;

	cin >> y >> dot_1 >> m >> dot_2 >> d;


	cout.width(4);
	cout.fill('0');
	cout << y << dot_1;
	
	cout.width(2);
	cout.fill('0');
	cout << m << dot_2;
	
	cout.width(2);
	cout.fill('0');
	cout << d << endl;

	return 0;

}
```
