#include <bits/stdc++.h>
using namespace std;

#define endl "\n"

int part1(const vector<string> &input) {
    vector<int> left;
    vector<int> right;

    for (const string &line : input) {
        istringstream stream(line);
        int firstNum, secondNum;
        stream >> firstNum >> secondNum;

        left.push_back(firstNum);
        right.push_back(secondNum);
    }

    sort(left.begin(), left.end());
    sort(right.begin(), right.end());

    long long t = 0;
    for (int i = 0; i < left.size(); i++) {
        t += abs(left[i] - right[i]);
    }

    return t;
}

int part2(const vector<string> &input) {
    vector<int> left;
    unordered_map<int, int> rightFreq;

    for (const string &line : input) {
        istringstream stream(line);
        int firstNum, secondNum;
        stream >> firstNum >> secondNum;

        left.push_back(firstNum);
        rightFreq[secondNum]++;
    }

    long long t = 0;
    for (int i = 0; i < left.size(); i++) {
        t += left[i] * rightFreq[left[i]];
    }

    return t;
}

int main() {
    ifstream inputFile("day1.txt");
    vector<string> inputLines;
    string line;
    
    while (getline(inputFile, line)) {
        inputLines.push_back(line);
    }

    cout << "Part 1: " << part1(inputLines) << endl;
    cout << "Part 2: " << part2(inputLines) << endl;
}