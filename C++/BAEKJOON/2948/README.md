## 문제
#### 2009년 날짜가 주어졌을 때, 무슨 요일인지 출력하는 프로그램을 작성하시오.

###### 입력
###### 첫째 줄에 D와 M이 주어진다. M월 D일이다.

###### 출력
###### 2009년 M월 D일의 요일을 영어로 출력한다. 출력은 다음 중 하나이다. "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday".



```c++
#include <iostream>

using namespace std;

int main() {

	int month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	int d, m;
	string day[7] = {"Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"};

	cin >> d >> m;

	for (int i = 1; i < m; i++) d += month[i];

	cout << day[d % 7] << "\n";
	

	return 0;

}
```
