#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a; int b;
    string charr[]={"","one", "two", "three", "four", "five", "six", "seven",       "eight", "nine" };
    cin >> a; cin >> b;
    for (int i=a; i<=b ; i++) {
        cout<<((i<=9)?charr[i]:((i%2==0)?"even":"odd"))<<endl;
    }
    return 0;
}
