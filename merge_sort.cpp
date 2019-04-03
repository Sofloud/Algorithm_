#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& first, vector<int>& second, vector<int>& newV) {
    size_t i = 0, j = 0;
    newV.reserve(first.size() + second.size());
    while (i < first.size() && j < second.size()) {
        if (first[i] < second[j]) {
            newV.push_back(first[i]);
            ++i;
        } else {
            newV.push_back(second[j]);
            ++j;
        }
    }
    if (i < first.size()) {
        while (i != first.size()) {
            newV.push_back(first[i]);
            ++i;
        }
    } else if (j < second.size()) {
        while (j != second.size()) {
            newV.push_back(second[j]);
            ++j;
        }
    }
}

int main() {
    int count, numberMed;
    cin >> count >> numberMed;
    vector<vector<int>> nums(count);

    for (int i = 0; i < count; ++i) {
        for (int j = 0; j < numberMed; ++j) {
            int a;
            cin >> a;
            nums[i].push_back(a);
        }
    }

    for (int i = 0; i < count; ++i) {
        for (int j = i + 1; j < count; ++j) {
            vector<int> result;
            merge(nums[i], nums[j], result);
            cout << result[numberMed - 1] << '\n';
        }
    }
}
