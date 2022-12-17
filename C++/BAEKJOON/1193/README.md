분수찾기
## 문제
#### 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
|||||||
|----|----|----|----|----|----|
|1/1|1/2|1/3|1/4|1/5|…|
|2/1|2/2|2/3|2/4|…|…|
|3/1|3/2|3/3|…|…|…|
|4/1|4/2|…|…|…|…|
|5/1|…|…|…|…|…|
|…|…|…|…|…|…|
#### 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
#### X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
###### 입력
###### 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.
###### 출력
###### 첫째 줄에 분수를 출력한다.

```c++
#include <iostream>

using namespace std;

int main() {

	int n, x, y;
	int val = 0;
	int num = 0;
	int line = 0;
	int i = 0;

	cin >> n;

	while (true) {

		num += i;
		
		if (line == 0) {

			if (num >= n) {

				line = i;
				//cout << "line: " << line << "\n";
				break;

			}
			else {

				i++;

			}
		
		}

	}

	if (line != 0) {

		if (line % 2 == 0) {

			for (int j = 0; j < line; j++) {

				val += j;
				//cout << "val: " << val << "\n";

			}

			x = n - val;
			y = line - (n - val) + 1;

			//cout << "n: " << n - val << "\n\n";

		}
		else if (line % 2 == 1) {

			for (int j = 0; j < line; j++) {

				val += j;
				//cout << "val: " << val << "\n";

			}

			y = n - val;
			x = line - (n - val) + 1;

			//cout << "n: " << n - val << "\n\n";

		}

	}

	cout << x << "\/" << y;

	return 0;

}
```
