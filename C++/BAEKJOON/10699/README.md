## 문제
#### 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.

###### 입력
###### 입력은 없다.

###### 출력
###### 서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.

```c++
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <ctime>

using namespace std;

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	time_t timer = time(NULL);
	struct tm* t = localtime(&timer);
	
	cout << t->tm_year + 1900 << "-";
	cout.width(2);
	cout.fill('0');
	cout << t->tm_mon + 1 << "-";
	cout.width(2);
	cout.fill('0');
	cout << t->tm_mday;

	return 0;

}
```
