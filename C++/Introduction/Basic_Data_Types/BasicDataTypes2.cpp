#include <iomanip>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int a;
    long b;
    char c;
    float d;
    double e;
    std::cin >> a >> b >> c >> d >> e;
    std::cout << a << "\n" << b << "\n" << c << endl;
    std::cout << std::fixed << std::setprecision(3) << d << endl;
    std::cout << std::fixed << std::setprecision(6) << e << endl;
    return 0;
}
