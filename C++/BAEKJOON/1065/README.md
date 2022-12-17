한수
## 문제
#### 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
###### 입력
###### 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
###### 출력
###### 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

```c++
#include <iostream>
#include <string>

using namespace std;

int Hansoo(int n) {

	int result = 0;

	if (n < 100) {
		return n;
	}
	else {

		result += 99;

		for (int i = 100; i <= n; i++) {

			string num = to_string(i);
			int len = num.length();
			int nums[4] = {};
			int d[3] = {};
			int cnt = 0;

			for (int j = 0; j < len; j++) {

				nums[j] = int(num[j]) - 48;

			}

			for (int j = 0; j < len - 1; j++) {

				d[j] = num[j + 1] - num[j];

			}

			int d_p = d[0];

			for (int j = 0; j < len - 1; j++) {

				if (d[j] == d_p) {
					cnt++;
				}

			}

			if (cnt == len - 1) {
				result++;
			}

		}

	}

	return result;
}

int main() {

	int n;

	cin >> n;

	cout << Hansoo(n);

	return 0;

}
```
