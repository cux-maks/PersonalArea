## 문제
#### 첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제

#### 별은 가운데를 기준으로 대칭이어야 한다.

###### 입력
###### 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

###### 출력
###### 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
```c++
#include <iostream>

using namespace std;

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int k = 0; k < n - i - 1; k++) cout << " ";
		for (int j = 0; j <= i*2; j++) cout << "*";
		cout << "\n";
	}
	return 0;

}
```
