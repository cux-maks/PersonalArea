## 문제
#### 어떤 사람의 C언어 성적이 주어졌을 때, 평점은 몇 점인지 출력하는 프로그램을 작성하시오.

#### A+: 4.3, A0: 4.0, A-: 3.7

#### B+: 3.3, B0: 3.0, B-: 2.7

#### C+: 2.3, C0: 2.0, C-: 1.7

#### D+: 1.3, D0: 1.0, D-: 0.7

#### F: 0.0

###### 입력
###### 첫째 줄에 C언어 성적이 주어진다. 성적은 문제에서 설명한 13가지 중 하나이다.

###### 출력
###### 첫째 줄에 C언어 평점을 출력한다.

```c++
#include <iostream>
#include <cctype>

using namespace std;

int main() {

	string str;
	cin >> str;

	if (str == "A+") cout << "4.3";
	else if (str == "A0") cout << "4.0";
	else if (str == "A-") cout << "3.7";
	else if (str == "B+") cout << "3.3";
	else if (str == "B0") cout << "3.0";
	else if (str == "B-") cout << "2.7";
	else if (str == "C+") cout << "2.3";
	else if (str == "C0") cout << "2.0";
	else if (str == "C-") cout << "1.7";
	else if (str == "D+") cout << "1.3";
	else if (str == "D0") cout << "1.0";
	else if (str == "D-") cout << "0.7";
	else if (str == "F") cout << "0.0";

	return 0;

}
```
