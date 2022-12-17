
## 문제
#### 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
#### 비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드라고 읽는다.)

###### \<c\>
```c
#include <stdio.h>

int main(){

int a, b;

scanf("%d %d", &a, &b);
printf("%d", a&b);

return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int a, b;

	cin >> a >> b;
	cout << (a & b) << endl;

	return 0;
}
```
