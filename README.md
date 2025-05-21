# DSA-HW-SparseMatrix

This program is representing and performing fundamental operations (addition, subtraction, and multiplication) on sparse matrices. The implementation focuses on memory and runtime optimization by storing only non-zero elements.


## Features

* **Sparse Matrix Representation:** it uses a dictionary (hash map) to store only the non-zero elements along with their row and column indices, optimizing memory usage for large sparse matrices.

* **Matrix Operations:**
    * **Addition:** 
    * **Subtraction:** 
    * **Multiplication:** 


* **Error Handling methods:** 
    * `FileNotFoundError`: If input files do not exist.
    * `ValueError`: For incorrect input file formats 
    * `IndexError`: For attempts to access or set elements outside matrix bounds.
    



## How to Run

1.  **Navigate to the `src` directory:**
    Open your terminal or command prompt and change your current directory to `dsa-HW-Sparsematrix/dsa/sparse_matrix/code/src`.

    ```bash
    cd dsa-HW-Sparsematrix/dsa/sparse_matrix/code/src
    ```

2.  **Execute the Python script:**
    Run the `sparsematrix.py` file using the Python interpreter.

    ```bash
    python sparsematrix.py
    
    The program will present a menu of operations and ask you to enter the file paths for the two sparse matrices.


## Code Structure

The core logic resides in `sparsematrix.py`:

* **`SparseMatrix` class:**
    * `__init__(self, *args)`: Constructor to initialize a sparse matrix from a file path or specified dimensions.
    * `_load_from_file(self, file_path)`: Private helper method to handle reading and parsing matrix data from a file, including custom format validation.
    * `getElement(self, currRow, currCol)`: Retrieves the element at a given position (returns 0 if not explicitly stored).
    * `setElement(self, currRow, currCol, value)`: Sets or updates the element at a given position. If `value` is 0, it removes the entry from storage.
* **Utility Functions (outside the class):**
    * `add_sparse_matrices(matrix1, matrix2)`: Performs matrix addition.
    * `subtract_sparse_matrices(matrix1, matrix2)`: Performs matrix subtraction.
    * `multiply_sparse_matrices(matrix1, matrix2)`: Performs matrix multiplication.
    * `print_sparse_matrix(matrix)`: Helper function to display a sparse matrix in a readable grid format.
* **Main Execution Block (`if __name__ == "__main__":`)**
    * Handles user interaction, loads matrices, calls appropriate operation functions, and manages error reporting.


---
**References:** 
This project was developed with insights and foundational knowledge from the following resources:
- * "Sparse Matrix Representation" on GeeksforGeeks - `https://www.geeksforgeeks.org/sparse-matrix-representation/`
- * "Python String Methods Tutorial" on Real Python - `https://realpython.com/python-string-methods/`
- * "Data structure|Strings|Sparse matrix" by Engineering Education - `https://www.youtube.com/watch?v=VTaHoRyBmAQ`

