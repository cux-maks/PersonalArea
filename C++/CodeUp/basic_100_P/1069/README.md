
## 문제
#### 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

#### 평가 내용
#### 평가 : 내용
#### A : best!!!
#### B : good!!
#### C : run!
#### D : slowly~
#### 나머지 문자들 : what?

###### \<c\>
```c
#include <stdio.h>

int main() {

	char a;
	scanf("%c", &a);
	
	switch (a) {
	case 'A':
		printf("best!!!");
		break;
	case 'B':
		printf("good!!");
		break;
	case 'C':
		printf("run!");
		break;
	case 'D':
		printf("slowly~");
		break;
	default:
		printf("what?");
		break;
	}

	return 0;
}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	string grade, result;

	cin >> grade;

	result = grade == "A" ? "best!!!" : "what?";
	result = grade == "B" ? "good!!" : result;
	result = grade == "C" ? "run!" : result;
	result = grade == "D" ? "slowly~" : result;

	cout << result << endl;

	return 0;

}
```
