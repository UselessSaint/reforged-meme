#include <iostream>
#include "includes.h"
#include "matrix.h"

using namespace std;

int main()
{
	try
	{
		/*Matrix<int> m(2,3, {2, 3,
							4, 5});*/
							
		Matrix<int> m(3,3,	{1,2,3,
							 1,4,5,
							 1,6,7});
		m.printRows();/*
		
		m.elementAt(1,1) = 22;
		cout << m.elementAt(2,2) << endl;*/
		
		auto it = m.beginRow();
		auto iq = m.beginColumn();
		
		++it;
		++it;
		++iq;
		++iq;
		++iq;
		
		auto t = *it;
		
		*it = *iq;
		*iq = t;
		cout << "---------" << endl;
		m.printRows();
		//m.printRows();
		//cout << "---------" << endl;
		//m.printColumns();
/*
		Matrix<double> q(5,5,  {1.2,2.2,3.2,4.2,5.2,
								1,2,3,4,5,
								1,2,3,4,5});*/
		//cout << "---------" << endl;
		//q.printRows();
		//cout << "---------" << endl;
		//q.printColumns();
		
		
		//m.elementAt(1,1) = 22;
	}
	catch (exception& exc)
	{
		cout << exc.what() << endl;
	}


    return 0;
}
