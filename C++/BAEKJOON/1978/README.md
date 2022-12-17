소수 찾기
## 문제
#### 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
###### 입력
###### 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

###### 출력
###### 주어진 수들 중 소수의 개수를 출력한다.

```c++
#include <iostream>
#include <vector>

using namespace std;

int main() {

	int n;
	int cnt = 0;
	vector<int> v;

	cin >> n;

	for (int i = 0; i < n; i++) {

		int a;
		int val = 0;

		cin >> a;

		v.push_back(a);

		if (v[i] == 2) {

			cnt++;

		}
		else {

			for (int j = 1; j <= a; j++) {

				val = v[i] % j == 0 ? val + 1 : val;

			}

			cnt = val == 2 ? cnt + 1 : cnt;

		}

	}

	cout << cnt;

	return 0;

}
```
