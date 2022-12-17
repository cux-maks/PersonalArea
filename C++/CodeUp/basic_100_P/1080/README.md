
## 문제
#### 1, 2, 3 ... 을 계속 더해 나갈 때,
#### 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지
#### 계속 더하는 프로그램을 작성해보자.

#### 즉, 1부터 n까지 정수를 계속 더한다고 할 때,
#### 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.

###### \<c\>
```c
#include <stdio.h>

int main(){

  int a;

  int i = 1, b = 0;

  scanf("%d", &a);

  while(1){
    b = b + i;
    if(b >= a){
        printf("%d", i);
        break;
    }
    i++;
  }

return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int a;
	int i = 0;
	int result = 0;

	cin >> a;

re:
	
	result = result + i;
	
	if (result >= a) {

		goto end;

	}
	else {

		i++;
		goto re;

	}

end:

	cout << i << endl;

	return 0;

}

```
