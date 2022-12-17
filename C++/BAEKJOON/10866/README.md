덱
## 문제
#### 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

#### 명령은 총 여덟 가지이다.

#### 1.push_front X: 정수 X를 덱의 앞에 넣는다.
#### 2.push_back X: 정수 X를 덱의 뒤에 넣는다.
#### 3.pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#### 4.pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#### 5.size: 덱에 들어있는 정수의 개수를 출력한다.
#### 6.empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
#### 7.front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#### 8.back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
###### 입력
###### 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

###### 출력
###### 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

```c++
#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int n;
	deque<int> dq;

	cin >> n;
	cin.ignore();

	for (int i = 0; i < n; i++) {

		string command;

		getline(cin, command);

		if (command.find("push_front") != string::npos) {

			command.erase(0, 10);
			dq.push_front(stoi(command));

		}
		else if (command.find("push_back") != string::npos) {

			command.erase(0, 9);
			dq.push_back(stoi(command));

		}
		else if (command.find("pop_front") != string::npos) {

			auto it = dq.empty() ? -1 : dq.front();
			cout << it << "\n";
			
			if (!dq.empty()) {

				dq.pop_front();

			}

		}
		else if (command.find("pop_back") != string::npos) {

			auto it = dq.empty() ? -1 : dq.back();
			cout << it << "\n";
			
			if (!dq.empty()) {

				dq.pop_back();

			}

		}
		else if (command.find("size") != string::npos) {

			cout << dq.size() << "\n";

		}
		else if (command.find("empty") != string::npos) {

			auto it = dq.empty() ? 1 : 0;
			cout << it << "\n";

		}
		else if (command.find("front") != string::npos) {

			auto it = dq.empty() ? -1 : dq.front();
			cout << it << "\n";

		}
		else if (command.find("back") != string::npos) {

			auto it = dq.empty() ? -1 : dq.back();
			cout << it << "\n";

		}

	}

	return 0;

}
```
