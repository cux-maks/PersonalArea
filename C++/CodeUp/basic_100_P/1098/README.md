
## 문제
#### 부모님과 함께 유원지에 놀러간 영일이는
#### 설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

#### 길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

#### 막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
#### (잉어, 붕어, 용 등 여러 가지가 적혀있다.)


![image](https://user-images.githubusercontent.com/82014995/172887593-afc28ca4-9d69-4dcc-b32f-062926ad1519.png)



#### 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
#### 막대를 놓는 방향(d:가로는 0, 세로는 1)과
#### 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

#### 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int pad[101][101] = {};
	int h, w, n, l, d, x, y;

	scanf("%d %d", &h, &w);
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d %d %d", &l, &d, &y, &x);
		if (d == 0) {
			for (int k = 0; k < l; k++) {
				pad[y][x + k] = 1;
			}
		}
		if (d == 1) {
			for (int j = 0; j < l; j++) {
				pad[y + j][x] = 1;
			}
		}
	}

	for (int i = 1; i <= h; i++) {
		for (int j = 1; j <= w; j++) {
			printf("%d ", pad[i][j]);
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

	bool board[101][101] = {};
	int w, h, n, l, d, x, y;
	int x_p = 0;
	int y_p = 0;

	cin >> w >> h >> n;

	for (int i = 0; i < n; i++) {

		cin >> l >> d >> x >> y;

		for (int j = 0; j < l; j++) {

			board[x + x_p][y + y_p] = !board[x + x_p][y + y_p];
			x_p = d == 1 ? x_p + 1 : x_p;
			y_p = d == 0 ? y_p + 1 : y_p;

		}

		x_p = 0;
		y_p = 0;

	}

	for (int i = 1; i <= w; i++) {

		for (int j = 1; j <= h; j++) {
			
			cout << board[i][j] << " ";

		}

		cout << "\n";

	}

	return 0;

}
```
