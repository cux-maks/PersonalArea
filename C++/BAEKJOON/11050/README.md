이항 계수 1
## 문제
#### 자연수 ![image](https://user-images.githubusercontent.com/82014995/172145237-cad948ea-a5f3-460d-b471-d3c2421dc13a.png)과 정수 ![image](https://user-images.githubusercontent.com/82014995/172145294-ae0e9161-52fe-4668-9ac7-c207491ed838.png)가 주어졌을 때 이항 계수 ![image](https://user-images.githubusercontent.com/82014995/172145326-19f2a556-c6c1-4c6e-8787-a38a1c583d1d.png)를 구하는 프로그램을 작성하시오.

###### 입력
###### 첫째 줄에 ![image](https://user-images.githubusercontent.com/82014995/172145251-7f2dfc2e-f0a2-4b57-93a9-7ced60d14396.png)과 ![image](https://user-images.githubusercontent.com/82014995/172145301-db8b846a-78bd-43ca-8519-d6cb9fb61604.png)가 주어진다. (1 ≤ ![image](https://user-images.githubusercontent.com/82014995/172145262-348ec3c3-c943-4086-8dd5-1de8e01e1aca.png)(1 ≤ 10, 0 ≤ ![image](https://user-images.githubusercontent.com/82014995/172145305-ead38f41-fcd9-4b1c-a198-8e5482daaf0a.png) ≤ ![image](https://user-images.githubusercontent.com/82014995/172145273-06eb1cbe-4885-4520-9056-0d12506ef4eb.png))

###### 출력
 
###### ![image](https://user-images.githubusercontent.com/82014995/172145330-3ff4532e-32e7-4f82-bce6-d67d6bb0dc54.png)를 출력한다.

```c++
#include <iostream>
#include <cmath>

using namespace std;

int C(int n, int r) {

	if (n == r || r == 0) {

		return 1;

	}
	else {

		return C(n - 1, r - 1) + C(n - 1, r);

	}

}

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int n, r;

	cin >> n >> r;

	cout << C(n, r);

}
```
