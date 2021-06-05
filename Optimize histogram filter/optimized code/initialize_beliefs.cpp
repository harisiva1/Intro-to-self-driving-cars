#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector< vector <float> > initialize_beliefs(vector< vector <char> > &grid) {

	// OPTIMIZATION: Which of these variables are necessary?
	// OPTIMIZATION: Reserve space in memory for vectors
  	int height = grid.size();
	int width = grid[0].size();
  	vector< vector <float> > newGrid;
    newGrid.reserve(height);
	vector<float> newRow;
    newRow.reserve(width);
	//float total, prob_per_cell;

  	//float prob_per_cell = 1.0 / ( (float) height * width) ;

  	// OPTIMIZATION: Is there a way to get the same results 	// without nested for loops?
	
	for (int j=0; j<height; j++) {
		newRow.push_back(1.0 / ( (float) height * width));
		}
   for (int i=0; i<width; i++) {
		newGrid.push_back(newRow);
	}
	return newGrid;
}