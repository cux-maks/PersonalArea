1021
## 문제
#### 1개의 단어를 입력받아 그대로 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	char note[51] = "";
	scanf("%s", note);
	printf("%s", note);
	return 0;

}
```

###### \<c++\>
```c++
#define SIZE 51

#include <iostream>

using namespace std;

int main() {

	char word[SIZE];

	cin >> word;
	cout << word << endl;

	return 0;

}

```
