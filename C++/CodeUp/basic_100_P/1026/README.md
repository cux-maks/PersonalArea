
## 문제
#### 입력되는 시:분:초 에서 분만 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int h, m, s;
	scanf("%d:%d:%d", &h, &m, &s);
	printf("%d", m);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>
#include <string>

using namespace std;

int main() {

	string h, m, s;

	getline(cin, h, ':');
	getline(cin, m, ':');
	getline(cin, s);

	cout << stoi(m) << endl;

	return 0;

}
```
