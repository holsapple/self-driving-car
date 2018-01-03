#include "headers/normalize.h"
using namespace std;

vector< vector<float> > normalize(vector< vector <float> > &grid) {

	vector<int>::size_type height = grid.size();
	vector<int>::size_type width = grid[0].size();
	
	float total = 0.0;
	
	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			total += grid[i][j];
		}
	}

	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			grid[i][j] = grid[i][j] / total;
		}
	}

	return grid;
}
