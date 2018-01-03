#include "headers/initialize_beliefs.h"

using namespace std;

vector< vector <float> > initialize_beliefs(vector< vector <char> > &grid) {

	vector<int>::size_type height = grid.size();
	vector<int>::size_type width = grid[0].size();

  	float prob_per_cell = 1.0 / (height * width);
  	vector< vector<float> > newGrid (height, vector<float> (width, prob_per_cell));

	return newGrid;
}