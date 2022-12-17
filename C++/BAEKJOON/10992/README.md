## 문제
#### 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

###### 입력
###### 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

###### 출력
###### 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
```c++
#include <iostream>
using namespace std;

int main() {
	int num;
	cin >> num;
	for (int i = 1; i <= num; i++) {
		if (i == num) { for (int i = 1; i <= 2 * num - 1; i++) cout << "*"; }
		else {
			for (int j = num - i; j > 0; j--) { cout << " "; }
			cout << "*";
			if (i != 1) {
				for (int j = 1; j <= (i - 1) * 2 - 1; j++) { cout << " "; }
				cout << "*";
			}
		}
		cout << "\n";
	}
	return 0;
}
```
