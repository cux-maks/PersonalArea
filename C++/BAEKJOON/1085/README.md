직사각형에서 탈출
## 문제
#### 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
###### 입력
###### 첫째 줄에 x, y, w, h가 주어진다.
###### 출력
###### 첫째 줄에 문제의 정답을 출력한다.

```c++
#include <iostream>

using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int x, y, w, h;
	int min = 1000;

	cin >> x >> y >> w >> h;

	min = min > x ? x : min;
	min = min > w - x ? w - x : min;
	min = min > y ? y : min;
	min = min > h - y ? h - y : min;

	cout << min << "\n";

	return 0;

}
```
