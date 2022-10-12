#include <bits/stdc++.h>

using namespace std;

int main(){
	ifstream inFile("out.bin", ios::in | ios::binary);
	for(int i =0;i<10;i++)
	{
		int tmp;
		inFile.read((char*)&tmp,sizeof(int));
		cout<<tmp<<endl;
	}
	inFile.close();
	return 0;
}
