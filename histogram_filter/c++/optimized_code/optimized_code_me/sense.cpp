#include "headers/sense.h"

using namespace std;

vector< vector <float> > sense(char color, vector< vector <char> > &grid, vector< vector <float> > &beliefs,  float p_hit, float p_miss) {
	
	vector<int>::size_type height = beliefs.size();
	vector<int>::size_type width = beliefs[0].size();

	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			if (grid[i][j] == color) {
				beliefs[i][j] = beliefs[i][j] * p_hit;
			}
			else {
				beliefs[i][j] = beliefs[i][j] * p_miss;
			}
		}
	}
	return beliefs;
}
