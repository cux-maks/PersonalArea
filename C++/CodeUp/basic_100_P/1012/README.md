
## 문제
#### 실수형(float)로 변수를 선언하고 그 변수에 실수값을 저장한 후
#### 저장되어 있는 실수값을 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	float a;
	scanf("%f", &a);
	printf("%f", a);
	return 0;

}
```

###### \<c++\>
```c++
#include<iostream>
using namespace std;

int main(){
    double a;
    cin>>a;

    cout << fixed;
    cout<<a;
    cout.precision(7);

    return 0;
}

```
