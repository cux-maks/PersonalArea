
## 문제
#### 윈도우 운영체제의 파일 경로를 출력하는 연습을 해보자.
 
#### 파일 경로에는 특수문자들이 포함된다.

#### 다음 경로를 출력하시오.

#### "C:\Download\hello.cpp"
#### (단, 큰따옴표도 함께 출력한다.)

###### \<c\>
```c
#include <stdio.h>

int main() {

	printf("\"C:\\Download\\hello.cpp\"");
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	cout << "\"C:\\Download\\hello.cpp\"";

	return 0;

}

```
