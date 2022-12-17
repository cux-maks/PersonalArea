직각삼각형
## 문제
![image](https://user-images.githubusercontent.com/82014995/172139697-b8e52de1-22a7-41c2-9bb7-83f10f19034f.png)

#### 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

###### 입력
###### 입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

###### 출력
###### 각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.

```c++
#include <iostream>

using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	while (true) {

		int a, b, c;

		cin >> a >> b >> c;

		if (a == 0 && b == 0 && c == 0) {

			break;

		}

		if ((a * a + b * b - c * c == 0 || a * a - b * b + c * c == 0 || b * b - a * a + c * c == 0) && (a != 0 && b != 0 && c != 0)) {

			cout << "right\n";

		}
		else {

			cout << "wrong\n";

		}

	}

	return 0;

}
```
