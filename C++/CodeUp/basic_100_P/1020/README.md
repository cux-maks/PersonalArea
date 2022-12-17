
## 문제
#### 주민번호는 다음과 같이 구성된다.

#### XXXXXX-XXXXXXX

#### 앞의 6자리는 생년월일(yymmdd)이고 뒤 7자리는 성별, 지역, 오류검출코드이다.
#### 주민번호를 입력받아 형태를 바꿔 출력해보자.


###### \<c\>
```c
#include <stdio.h>

int main() {

	int y, m;
	scanf("%d-%d", &y, &m);
	printf("%06d%07d", y, m);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>
#include <string>

using namespace std;

int main() {

	string front, back;

	getline(cin, front, '-');
	getline(cin, back);

	cout << front << back << endl;

	return 0;
}

```
