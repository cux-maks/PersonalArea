
## 문제
#### 부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

#### "십(+)자 뒤집기를 해볼까?"하고 생각했다.

#### 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
#### n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int pad[20][20] = {};
	int n, x, y;
	for (int i = 1; i <= 19; i++) {
		for (int j = 1; j <= 19; j++) {
			scanf("%d", &pad[j][i]);
		}
	}
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &x, &y);
		for (int k = 1; k <= 19; k++) {
			pad[y][k] = !pad[y][k];
		}
		for (int j = 1; j <= 19; j++) {
			pad[j][x] = !pad[j][x];
		}
	}

	for (int i = 1; i <= 19; i++) {
		for (int j = 1; j <= 19; j++) {
			printf("%d ", pad[j][i]);
		}
		printf("\n");
	}

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

	for (int i = 0; i < 19; i++) {

		for (int j = 0; j < 19; j++) {

			cin >> checkerboard[i][j];

		}

	}

	cin >> n;

	for (int i = 0; i < n; i++) {

		cin >> x >> y;

		for (int i = 0; i < 19; i++) {

			checkerboard[x - 1][i] = !checkerboard[x - 1][i];
			checkerboard[i][y - 1] = !checkerboard[i][y - 1];

		}

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
