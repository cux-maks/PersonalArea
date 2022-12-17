벌집
## 문제
![](https://user-images.githubusercontent.com/82014995/172134805-e2c5422c-5ab2-419b-a221-9ac652a5b511.png)
#### 위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

###### 입력
###### 첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

###### 출력
###### 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

```c++
#include <iostream>

using namespace std;

int main() {

	long long int n;
	int cnt = 1;
	int i = 1;

	cin >> n;

	while (true) {

		long long int end = i == 1 ? 1 : 1 + ((6 + (6 + (i - 2) * 6))/2) * (i - 1);
		long long int start = i == 1 ? 1 : end - ((i - 1) * 6) + 1;

		/*cout << "start: " << start << "\n";
		cout << "end: " << end << "\n\n";*/

		if (n == 1) {

			break;

		}
		else if(n >= start && n <= end){

			break;

		}

		cnt++;
		i++;

	}

	cout << cnt;

	return 0;

}
```
