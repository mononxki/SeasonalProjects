#include <iostream>

using namespace std;

int main(){


double sum = 0;
double product = 1;
double n;
unsigned numberOfValues;


cout << "Enter number of values to compute: ";
cin >> numberOfValues;

for (unsigned i = 0; i < numberOfValues; i++)
{
    cout << "Enter number: ";
    cin >> n;

    sum += n;

    product *= n;

}

cout << "the sum is: " << sum << ", the product is: " << product << endl;

system("pause"); 
	return 0;
}