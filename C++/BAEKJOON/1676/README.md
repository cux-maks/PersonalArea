## 문제
#### N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

###### 입력
###### 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

###### 출력
###### 첫째 줄에 구한 0의 개수를 출력한다.



```c++
#include <iostream>

using namespace std;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int cnt = 0;
    int n;

    cin >> n;

    for (int i = 5; i <= n; i *= 5) {

        cnt += n / i;

    }

    cout << cnt;

    return 0;
}
```