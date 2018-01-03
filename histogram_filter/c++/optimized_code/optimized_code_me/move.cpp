#include "headers/move.h"
#include "headers/zeros.h"

using namespace std;

vector< vector <float> > move(int dy, int dx, vector< vector<float> > &beliefs) {

	vector<int>::size_type height = beliefs.size();
	vector<int>::size_type width = beliefs[0].size();
	vector< vector<float> > newGrid = zeros(height, width);
	
  	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			newGrid[(i + dy + height) % height][(j + dx + width)  % width] = beliefs[i][j];
		}
	}
	return newGrid;
}
