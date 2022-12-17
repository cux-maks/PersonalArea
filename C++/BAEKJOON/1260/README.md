## 문제
#### 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

###### 입력
###### 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

###### 출력
###### 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

```c++
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

void dfs(int x, vector<int> graph[], bool visited[]) {

    visited[x] = true;
    cout << x << " ";
    for (int i = 0; i < graph[x].size(); i++) {
        int y = graph[x][i];
        if (!visited[y]) dfs(y, graph, visited);
    }

}

void bfs(int x, vector<int> graph[], bool visited[]) {

    queue<int> q;

    q.push(x);
    visited[x] = true;

    while (!q.empty()) {
        int temp = q.front();
        q.pop();
        cout << temp << " ";
        for (int i = 0; i < graph[temp].size(); i++) {
            if (visited[graph[temp][i]] == false) {
                q.push(graph[temp][i]);
                visited[graph[temp][i]] = true;
            }
        }
    }

}

int main() {

    int n, m, v;
    
    cin >> n >> m >> v;

    vector<int>* graph = new vector<int>[n + 1];
    bool* visited = new bool[n + 1] {0};

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i <= n; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

    dfs(v, graph, visited);

    for (int i = 0; i < n + 1; i++) visited[i] = 0;
    cout << "\n";

    bfs(v, graph, visited);

    return 0;

}
```
