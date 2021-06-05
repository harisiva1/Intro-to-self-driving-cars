#include "headers/sense.h"

using namespace std;

// OPTIMIZATION: Pass larger variables by reference
vector< vector <float> > sense(char color, vector< vector <char> > &grid, vector< vector <float> > &beliefs,  float p_hit, float p_miss) 
{
	// OPTIMIZATION: Is the newGrid variable necessary?
  	// Could the beliefs input variable be updated directly?
  	int i, j;
	int height = grid.size();
	int width = grid[0].size();
  	//vector< vector <float> > newGrid;
    //newGrid.reserve(height);
	//vector<float> row, newRow;

	//float prior, p;



	for (i=0; i<height; i++) {
		//newRow.clear();
		for (j=0; j<width; j++) {			
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
