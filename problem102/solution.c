#include <stdio.h>

/*
Three distinct points are plotted at random on a Cartesian plane, for which 
-1000 <= x, y <= 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ 
does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file 
containing the co-ordinates of one thousand "random" triangles, find the number 
of triangles for which the interior contains the origin.
*/

int main(int argc, const char** argv)
{
	FILE *triangles = fopen("triangles.txt", "r");
	char line[30];

	int x1, y1;
	int x2, y2;
	int x3, y3;

	if (triangles != NULL)
	{
		while (fgets(line, sizeof(line), triangles) != NULL)
		{
			sscanf(line, "%d,%d,%d,%d,%d,%d\n", &x1, &y1, &x2, &y2, &x3, &y3);
			// replace the following printf line with something that checks 
            // whether origin is in current triangle, add a counter somewhere 
            // in here to keep a total
			printf("(%d, %d); (%d, %d); (%d, %d)\n", x1, y1, x2, y2, x3, y3);
		}
		fclose(triangles);
	}

	printf("%d\n", 0); // Ultimately change this to print only the answer

	return 0;
}


// Does the triangle given by (x1, y1), (x2, y2), (x3, y3) contain (0, 0)?
int is_origin_in_interior(int x1, int y1, int x2, int y2, int x3, int y3)
{
	return 0;
}
