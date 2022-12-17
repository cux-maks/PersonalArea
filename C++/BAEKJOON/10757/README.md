큰 수 A + B
## 문제
#### 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

###### 입력
###### 첫째 줄에 A와 B가 주어진다. (0 < A,B < 1010000)

###### 출력
###### 첫째 줄에 A+B를 출력한다.

```c++
#include <iostream>
#include <string>

using namespace std;

int main() {

	string a, b, result;

	cin >> a >> b;

	if (a.size() < b.size()) {

		string c;

		for (int i = 0; i < b.size() - a.size(); i++) {

			c += '0';

		}

		a = c + a;

	}
	else {

		string c;

		for (int i = 0; i < a.size() - b.size(); i++) {

			c += '0';

		}

		b = c + b;

	}

	int temp = 0;

	while (a.size() != 0 && b.size() != 0) {

		int a_last = a.back() - '0';
		int b_last = b.back() - '0';
		int remainder = (temp + a_last + b_last) % 10;

		temp = (temp + a_last + b_last) / 10;
		result = (char)(remainder + '0') + result;

		a.pop_back();
		b.pop_back();

	}
	
	if (temp) {

		result = (char)(temp + '0') + result;

	}

	cout << result << "\n";

	return 0;

}
```
