
## 문제
#### 16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
#### 영일(01)이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.

#### A, B, C, D, E, F 중 하나가 입력될 때,
#### 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
#### (단, A ~ F 까지만 입력된다.)

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%X", &a);
	for (int i = 1; i < 16; i++) {
		printf("%X*%X=%X\n", a, i, a * i);
	}
	return 0;
}
```

###### \<c++\>
```c++
#include<iostream>
using namespace std;
int main() {

    int x;
    cin >> hex >> x;

    for (int i = 1; i < 16; i++) {
        cout << hex << uppercase << x << "*" << i << "=" << x*i << "\n";
    }
    return 0;
}
```
