## 문제
#### N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

###### 입력
###### 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

###### 출력
###### M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

```c++
#include <iostream>

using namespace std;

void quickSort(int i, int j, int arr[]) {

    if (i >= j) return;
    int pivot = arr[(i + j) / 2];
    int left = i;
    int right = j;

    while (left <= right) {
        while (arr[left] < pivot) left++;
        while (arr[right] > pivot) right--;
        if (left <= right) {
            swap(arr[left], arr[right]);
            left++;
            right--;
        }
    }

    quickSort(i, right, arr);
    quickSort(left, j, arr);
    
}

bool binSearch(int* arr, int len, int key) {

    int start = 0;
    int end = len - 1;
    int mid;

    while (end - start >= 0) {
        mid = (start + end) / 2;
        if (arr[mid] == key) {
            return true;
        }
        else if (arr[mid] > key) {
            end = mid - 1;
        }
        else {
            start = mid + 1;
        }
    }

    return false;

}

int main() {

    int n;

    cin >> n;

    int* nums = new int[n];

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int m;

    cin >> m;

    int* find = new int[m];

    for (int i = 0; i < m; i++) {
        cin >> find[i];
    }

    quickSort(0, n - 1, nums);

    for (int i = 0; i < m; i++) {
        cout << binSearch(nums, n, find[i]) << "\n";
    }
    return 0;
}
```
