#include<bits/stdc++.h>

using namespace std;

vector<vector<int>> graph;

int main() {
    int n;
    cin >> n;
    ::graph.resize(n);

    for (size_t i = 0; i != n; ++i) {
        for (size_t j = 0; j != n; ++j) {
            int a;
            cin >> a;
            graph[i].push_back(a);
        }
    }
    int length = 0;
    string res = "";
    for (size_t i = 1; i != pow(2, n); ++i) {
        bitset<20> number(i);
        string s = number.to_string();
        int cur_length = 0;
        for (int j = 20-n; j != 20; ++j) {
            if (s[j] == '0') {
                for (int k = 20-n; k != 20; ++k) {
                    if (s[k] == '1') {
                        cur_length = cur_length + graph[j-20+n][k-20+n];
                    }
                }
            }
        }
        if (cur_length > length) {
            length = cur_length;
            res = s;
        }
    }
    cout << length << '\n';
    for (size_t i = 20-n; i != res.size(); ++i) {
        if (res[i] == '0') {
            cout << 2 << ' ';
        } else if (res[i] == '1') {
            cout << 1 << ' ';
        }
    }
}