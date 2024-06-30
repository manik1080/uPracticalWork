#include <iostream>
#define CMP(a, b)(a > b) ? true : false
using namespace std;

class Knapsack {
    typedef struct {
        int v;
        int w;
        float r;
    }
    Item;
    int n, W;
    float current_weight = 0, current_value = 0;
    Item items[20];
    public:
        Knapsack() {
            cout << "Enter number of items: ";
            cin >> n;
            cout << "Enter capacity of knapsack: ";
            cin >> W;
            cout << "Enter Values:";
            for (int i = 0; i < n; i++) {
                cout << "\nV[" << i << "]: ";
                cin >> items[i].v;
            }
            cout << "Enter Weights:";
            for (int i = 0; i < n; i++) {
                cout << "\nW[" << i << "]: ";
                cin >> items[i].w;
            }
            // SORTING
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if (items[j].r < items[i].r) {
                        Item temp = items[j];
                        items[j] = items[i];
                        items[i] = temp;
                    }
                }
            }
        }
    float maxValue() {
        for (int i = 0; i < n; i++) {
            if ((current_weight + items[i].w) < W) {
                current_value += items[i].v;
                current_weight += items[i].w;
            } else {
                int wt = W - current_weight;
                current_value += (wt * items[i].r);
                current_weight += wt;
                break;
            }
        }
        return current_value;
    }
};
int main() {
    Knapsack k;
    cout << "The maximum value that can be stored is: " << k.maxValue();
    return 0;
}
