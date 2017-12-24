// You are given an n x n 2D matrix representing an image.

// Rotate the image by 90 degrees (clockwise).

// Follow up:
// Could you do this in-place?



public class rotateImg {
	
	public static void rotate(int[][] matrix) {

		// store rows to be turned into columns
		final int n = matrix.length;
		int[][] rows = new int[n][n];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {

				rows[i][j] = matrix[i][j];
				System.out.println(Integer.toString(rows[i][j]));
				
			}
		}

		for (int i = 0; i < n; i++) {

			rows[]

		}



	} // end of rotate

	public static void main(String[] args) {

		int[][] matrix = new int[3][3];

		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				matrix[i][j] = i * j;
			}
		}

		rotate(matrix);
		
	} // end of main

} // end of class