수 정렬하기
## 문제
#### N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

###### 입력
###### 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

###### 출력
###### 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

```c++
#include <iostream>

using namespace std;

int main() {

	int n;
	int num[1000] = {};

	cin >> n;

	for (int i = 0; i < n; i++) {

		cin >> num[i];

	}

	for (int i = 0; i < n; i++) {

		for (int j = 0; j < n - i - 1; j++) {

			if (int(num[j]) - '0' > (num[j + 1] - '0')) {

				int temp = num[j];
				num[j] = num[j + 1];
				num[j + 1] = temp;

			}

		}

	}

	for (int i = 0; i < n; i++) {

		cout << num[i] << "\n";

	}

	return 0;

}
```
