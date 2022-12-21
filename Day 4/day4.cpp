#include <bits/stdc++.h>
#include <fstream>
#include <string>
using namespace std;

int total = 0;

void solve(string lines)
{	
	int size = 0;
	string temp;

	for(char l : lines)
	{
		if (l == '\n')
		{
			++size;
		}
	}

	string allLines[size];
	int idx = 0;
	for(char x : lines)
	{	
		if (x == '\n')
		{
			allLines[idx] = temp;
			++idx;
			temp = "";
			continue;
		}
		temp += x;
	}

	string range1a = "";
	string range1b = "";
	string range2a = "";
	string range2b = "";

	for(string ranges : allLines)
	{	

		string tmpRange;
		string tmpRange2;

		for(char c : ranges)
		{	
			if (c == ',')
			{	
				for (char r: tmpRange)
				{
					if (r == '-')
					{	
						range1a += tmpRange2;
						tmpRange2 = "";
						continue;
					}
					tmpRange2 += r;
				}
				range1b = tmpRange2;
				tmpRange = "";
				continue;
			}
			tmpRange += c;
		}
		tmpRange2 = "";
		for (char r: tmpRange)
		{
			if (r == '-')
			{	
				range2a += tmpRange2;
				tmpRange2 = "";
				continue;
			}
			tmpRange2 += r;
		}
		range2b = tmpRange2;

		// cout << range1a << '-' << range1b <<' ' <<range2a << '-' << range2b << endl;
		if ((stoi(range1a) < stoi(range2a)) && (stoi(range1b) > stoi(range2b)))
		{
			::total++;
		} else if ((stoi(range2a) < stoi(range1a)) && (stoi(range2b) > stoi(range1b)))
		{
			::total++;
		}
		range1a = "";
		range1b = "";
		range2a = "";
		range2b = "";
	}
	cout << '\n';
}

int main()
{	

	string lines, line;
	ifstream File("input.txt");
	while(getline(File, line))
	{
		lines += line + "\n";
	}

	solve(lines);

	cout << ::total;

	return 0;
}