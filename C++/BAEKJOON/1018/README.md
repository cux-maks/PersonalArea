체스판 다시 칠하기
## 문제
#### 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
#### 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
#### 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8\*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
###### 입력
###### 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.
###### 출력
###### 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

```c++
#include <iostream>

using namespace std;

int main() {

	int n, m;
	int x = 0;
	int y = 0;
	int min = 2500;
	int count = 0;
	bool board[50][50] = {};

	cin >> n >> m;

	for (int i = 0; i < n; i++) {

		for (int j = 0; j < m; j++) {

			char state;

			cin >> state;

			board[i][j] = state == 'B' ? 0 : 1;

		}

	}

	for (int x = 0; x <= n - 8; x++) {

		for (int y = 0; y <= m - 8; y++) {

			for (int i = 0; i < 8; i++) {

				for (int j = 0; j < 8; j++) {

					if ((x + i) % 2 == 0 && (y + j) % 2 == 0 && board[x + i][y + j] != 1) {

						count += 1;
						// cout << "case 1: " << x << " " << y << " " << x + i << " " << y + j << "\n";

					}
					else if ((x + i) % 2 == 1 && (y + j) % 2 == 1 && board[x + i][y + j] != 1) {

						count += 1;
						// cout << "case 2: " << x << " " << y << " " << x + i << " " << y + j << "\n";

					}
					else if ((x + i) % 2 == 1 && (y + j) % 2 == 0 && board[x + i][y + j] != 0) {

						count += 1;
						// cout << "case 3: " << x << " " << y << " " << x + i << " " << y + j << "\n";

					}
					else if ((x + i) % 2 == 0 && (y + j) % 2 == 1 && board[x + i][y + j] != 0) {

						count += 1;
						// cout << "case 4: " << x << " " << y << " " << x + i << " " << y + j << "\n";

					}

				}

			}

			min = min < count ? min : count;
			count = 0;
			// cout << x << " " << y << " " << min << "\n";

			for (int i = 0; i < 8; i++) {

				for (int j = 0; j < 8; j++) {

					if ((x + i) % 2 == 0 && (y + j) % 2 == 0 && board[x + i][y + j] != 0) {

						count += 1;
						// cout << "case 5: " << x << " " << y << " " << x + i << " " << y + j << "\n";

					}
					else if ((x + i) % 2 == 1 && (y + j) % 2 == 1 && board[x + i][y + j] != 0) {

						count += 1;
						// cout << "case 6: " << x << " " << y << " " << x + i << " " << y + j << "\n";

					}
					else if ((x + i) % 2 == 1 && (y + j) % 2 == 0 && board[x + i][y + j] != 1) {

						count += 1;
						// cout << "case 7: " << x << " " << y << " " << x + i << " " << y + j << "\n";

					}
					else if ((x + i) % 2 == 0 && (y + j) % 2 == 1 && board[x + i][y + j] != 1) {

						count += 1;
						// cout << "case 8: " << x << " " << y << " " << x + i << " " << y + j << "\n";

					}

				}

			}

			min = min < count ? min : count;
			count = 0;
			// cout << x << " " << y << " " << min << "\n";

		}

	}

	cout << min;

	return 0;

}
```
