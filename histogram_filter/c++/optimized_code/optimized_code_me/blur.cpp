#include "headers/blur.h"
#include "headers/zeros.h"

using namespace std;

vector < vector <float> > blur(vector < vector < float> > &grid, float blurring) {

	vector<int>::size_type height = grid.size();
	vector<int>::size_type width = grid[0].size();
	vector< vector<float> > newGrid = zeros(height, width);

	static float center = 1.0 - blurring;
	static float corner = blurring / 12.0;
	static float adjacent = blurring / 6.0;
	static vector< vector<float> > window = {{corner, adjacent, corner}, {adjacent, center, adjacent}, {corner, adjacent, corner}};
	static vector<int> DX = {-1, 0, 1};
	static vector<int> DY = {-1, 0, 1};

	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			for (int ii = 0; ii < 3; ii++) {
				for (int jj = 0; jj < 3; jj++) {
					newGrid[(i + DY[ii] + height) % height][(j + DX[jj] + width) % width] += grid[i][j] * window[ii][jj];
				}
			}
		}
	}

	return newGrid;
}
