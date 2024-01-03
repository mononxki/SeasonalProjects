#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{

	double suma = 0, // addition
	liczba; // b
	unsigned int n; // no. ammount

	cout<<"Amount of numbers you want to use: ";
	cin>>n;
	
	cout<<endl;

	if(n>0) //  only +
	{
		for(int i = 1;i<= n;i++)
		{
			cout<<"Provide your number: ";
			cin>>liczba;
			suma+=liczba; 
		}
		cout<<"Arithmetic Average  "<<n<<" number(s) is: "<<suma/n<<endl;
	}
	else
		cout<<"Wrong Argument (N)"<<endl;

	system("pause"); 
	return 0;
	
}