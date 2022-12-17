1022
## 문제
#### 공백 문자가 포함되어 있는 문장을 입력받고 그대로 출력하는 연습을 해보자.

###### \<c\>
```c
#include <stdio.h>

int main(){

char a[2001]="";
fgets(a, 2000, stdin);
printf("%s", a);
return 0;

}
```

###### \<c++\>
```c++
#define SIZE 2001

#include <iostream>

using namespace std;

int main() {

	char line[SIZE];

	cin.getline(line, SIZE);
	cout << line << endl;

	return 0;

}

```
