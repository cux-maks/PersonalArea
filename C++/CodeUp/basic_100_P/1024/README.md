1024
## 문제
#### 단어를 1개 입력받는다.

#### 입력받은 단어(영어)의 각 문자를

#### 한줄에 한 문자씩 분리해 출력한다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	char a[21] = "";
	scanf("%s", a);
	for (int i = 0; a[i] != '\0'; i++) {
		printf("\'%c\'\n", a[i]);
	}
	return 0;

}
```

###### \<c++\>
```c++
#define SIZE 21

#include <iostream>

using namespace std;

int main() {
	
	char word[SIZE];

	cin >> word;

	for (int i = 0; word[i] != '\0'; i++) {
		cout << "'" << word[i] << "'" << endl;
	}

	return 0;

}
```
