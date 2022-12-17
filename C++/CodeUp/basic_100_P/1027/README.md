
## 문제
#### 년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.

#### 년월일(yyyy.mm.dd)를 입력받아,

#### 일월년(dd-mm-yyyy)로 출력해보자.

#### (단, 한 자리 일/월은 0을 붙여 두자리로, 년도도 0을 붙여 네자리로 출력한다.) 

###### \<c\>
```c
#include <stdio.h>

int main() {

	int y, m, d;
	scanf("%d.%d.%d", &y, &m, &d);
	printf("%02d-%02d-%04d", d, m, y);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>
#include <string>

using namespace std;

int main() {

	string y, m, d;

	getline(cin, y, '.');
	getline(cin, m, '.');
	getline(cin, d);

	cout.width(2);
	cout.fill('0');
	cout << stoi(d);

	cout.width(1);
	cout << "-";

	cout.width(2);
	cout << stoi(m);
	cout << "-";

	cout.width(4);
	cout << stoi(y) << endl;

	return 0;

}

```
