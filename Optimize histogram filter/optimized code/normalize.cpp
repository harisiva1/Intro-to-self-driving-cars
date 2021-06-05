#include "headers/normalize.h"
#include "headers/zeros.h"
using namespace std;

// OPTIMIZATION: Pass variable by reference
vector< vector<float> > normalize(vector< vector <float> > &grid) {

  	// OPTIMIZATION: Avoid declaring and defining 				// intermediate variables that are not needed.
	int height = grid.size();
    int width = grid[0].size();
    float total = 0.0;
	//vector<float> row;
	//vector<float> newRow;
	//float oldProb;
	for (int i = 0; i < height; i++)
	{
		//row = grid[i];
		for (int j=0; j< width; j++)
		{
			//oldProb = row[j];
			total += grid[i][j];
		}
	}

	vector< vector<float> > newGrid;
    newGrid = zeros(height,width);

	for (int i = 0; i < height; i++) {
		//vector<float> row = grid[i];
		//newRow.clear();
		for (int j=0; j< width; j++) {
			//float oldProb = row[j];
			//float newProb = oldProb / total;
			//newRow.push_back(newProb);
            newGrid[i][j] = grid[i][j]/total;
		}
		//newGrid.push_back(newRow);
	}

	return newGrid;
}
