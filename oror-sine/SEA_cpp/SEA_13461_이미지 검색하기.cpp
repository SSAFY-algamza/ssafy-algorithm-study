#define MAX_N (10000)
#define MAX_M (10)
#include<bitset>
using namespace std;

#include <iostream>

int _N, _M;
bitset<100> bitsList[10000];

void init(int N, int M, char mImageList[MAX_N][MAX_M][MAX_M])
{
	_N = N; _M = M;
	for (int i = 0; i < N; i++) {
		bitsList[i].reset();
		for (int r = 0; r < M; r++) {
			for (int c = 0; c < M; c++) {
				if (mImageList[i][r][c])
					bitsList[i].set(r*M + c);
			}
		}
	}
}
int findImage(char mImage[MAX_M][MAX_M])
{
	int min_id = 0;
	int min_cnt = 100;
	bitset<100> bits;
	for (int r = 0; r < _M; r++) {
		for (int c = 0; c < _M; c++) {
			if (mImage[r][c])
				bits.set(r*_M + c);
		}
	}
	for (int i = 0; i < _N; i++) {
		int cnt = (bitsList[i] ^ bits).count();
		if (min_cnt > cnt) {
			min_id = i + 1;
			min_cnt = cnt;
		}
	}


	return min_id;
}