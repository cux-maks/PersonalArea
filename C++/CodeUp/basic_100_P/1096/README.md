
## 문제
#### 기숙사 생활을 하는 학교에서 어떤 금요일(전원 귀가일)에는 모두 집으로 귀가를 한다.

#### 오랜만에 집에 간 영일이는 아버지와 함께 두던 매우 큰 오목에 대해서 생각해 보다가
#### "바둑판에 돌을 올린 것을 프로그래밍 할 수 있을까?"하고 생각하였다.

#### 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
#### n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

###### \<c\>
```c
#include <stdio.h>

int xy[20][20] = {};

int pad() {

	for (int i = 1; i <= 19; i++) {
		for (int j = 1; j <= 19; j++) {
			printf("%d ", xy[j][i]);
		}
		printf("\n");
	}
	return 0;

}

int main() {

	int n, x, y;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &x, &y);
		xy[y][x] = 1;
	}
	pad();
	
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int n, x, y;
	bool checkerboard[20][20] = {};

	cin >> n;
	
	for (int i = 0; i < n; i++) {

		cin >> x >> y;

		checkerboard[x - 1][y - 1] = 1;

	}

	for (int i = 0; i < 19; i++) {

		for (int j = 0; j < 19; j++) {

			cout << checkerboard[i][j] << " ";

		}

		cout << "\n";

	}

	return 0;

}
```
