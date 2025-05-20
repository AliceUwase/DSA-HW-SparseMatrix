class SparseMatrix:
    def __init__(self, *args):
        self.rows = 0
        self.cols = 0
        self.data = {}

        if len(args) == 1:
            file_path = args[0]
            self._load_from_file(file_path)
        elif len(args) == 2:
            num_rows, num_cols = args
            if not isinstance(num_rows, int) or not isinstance(num_cols, int) or num_rows < 0 or num_cols < 0:
                raise ValueError("Number of rows and colums must be positive integers!")
            self.rows = num_rows
            self.cols = num_cols

        else:
            raise ValueError("Invalid number of argumemnts, use SparseMatrix(filepath) or SparseMatrix(num_rows, num_cols)")

    def _load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()

                if not lines:
                    raise ValueError("Input file is empty!")
                
                dimension_line = lines[0].strip()
                parts = dimension_line.split(',')
                rows_found = False
                cols_found = False
                for part in parts:
                    sub_parts = part.strip().split('=')
                    if len(sub_parts) == 2:
                        key = sub_parts[0].strip()
                        value_str = sub_parts[1].strip()
                        try:
                            value = int(value_str)
                            if key == 'rows':
                                self.rows = value
                                rows_found = True 
                            elif key == 'cols':
                                self.cols = value 
                                cols_found = True
                        except ValueError:
                            raise ValueError("Input file has a wrong format. Rows and Cols should be integers!")
                    else:
                        raise ValueError("Input file has a wrong format. Expected 'rows=int' and cols=int' on first line!")
                    
                if not rows_found or not cols_found:
                    raise ValueError("Input file has a wrong format. First lineshould ecify both 'rows' and 'cols'!")
                
                data_lines = lines[1:]
                for line in data_lines:
                    line = line.strip()
                    if not line:
                        continue

                    if line.startswith('(') and line.endswith(')'):
                        content = line[1:-1].strip()
                        values = content.split(',')
                        if len(values) == 3:
                            try:
                                row = int(values[0].strip())
                                col = int(values[1].strip())
                                value = float(values[2].strip())
                                if 0 <= row < self.rows and 0 <= col < self.cols:
                                    if value != 0:
                                        self.data[(row, col)] = value 
                                    else:
                                        raise ValueError(f"Row or Column index out of bounds: ({row}, {col} for matrix of sizee ({self.rows}, {self.cols})")
                            except ValueError:
                                raise ValueError("Input file has wrong format. Excepted ' (row, col, value)' with integer values.")
                        else: 
                            raise ValueError("Input file has wrong format. Expected '(row, col, value)'")
                    elif line:
                        raise ValueError("Input file has wrong format. Non-empty lines should be format '(row, col, value)'")
                    
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: Input file '{file_path}' not found! ")
        except ValueError as e:
            raise ValueError(f"Error loading matrix from '{file_path}': {e}")
        except Exception as e:
            raise Exception(f"unexpected error occured while loading  matricx from '{file_path}': {e}")
    pass  

    def getElement(self, currRow, currCol):
        if not (0 <= currRow < self.rows and 0 <= currCol < self.cols):
            raise IndexError("Row or column index is out of limit!")
        return self.data.get((currRow, currCol), 0)
    
    def setElement(self, currRow, currCol, value):
        if not (0 <= currRow < self.rows and 0 <= currCol < self.cols):
            raise IndexError("Row or column index is out of limit!")
        if value != 0:
            self.data[(currRow, currCol)] = value 
        elif (currRow, currCol) in self.data:
            del self.data[(currRow, currCol)]

    @staticmethod
    def sparseMatrix_addition(matrix1, matrix2):
        if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
            raise ValueError("Matrices need to have the same dimensions for addition!")
        result = SparseMatrix(matrix1.rows, matrix1.cols)

        # adding elements from matrix1 and setting them in the result matrix
        for (r, c), val in matrix1.data.items():
            result.setElement(r, c, val)
            
        # adding elements from matrix2, combining them with existing values from matrix1
        for (r, c), val in matrix2.data.items():
            current_val = result.getElement(r, c)
            result.setElement(r, c, current_val + val)
        

    @staticmethod
    def sparseMatrix_subtraction(matrix1, matrix2):
        if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
            raise ValueError("Matrices need to have the same dimensions for subtraction!")
            
        result = SparseMatrix(matrix1.rows, matrix1.cols)
        
        # Add all elements from matrix1
        for (r, c), val in matrix1.data.items():
            result.setElement(r, c, val)
            
        # Subtract elements from matrix2
        for (r, c), val in matrix2.data.items():
            current_val = result.getElement(r, c)
            result.setElement(r, c, current_val - val)
            
        return result
        
    @staticmethod
    def sparseMatrix_multiplication(matrix1, matrix2): 
        if matrix1.cols != matrix2.rows:
            raise ValueError("Number of columns in first matrix must be equal to number of rows in second matrix for multiplication!")
            
        result = SparseMatrix(matrix1.rows, matrix2.cols)
        
        # For each non-zero element in matrix1
        for (r1, c1), val1 in matrix1.data.items():
            # For each non-zero element in matrix2 that can multiply with val1
            for (r2, c2), val2 in matrix2.data.items():
                if c1 == r2:  # If multiplication is possible
                    product = val1 * val2
                    current = result.getElement(r1, c2)
                    result.setElement(r1, c2, current + product)
                    
        return result
    @staticmethod
    def display_SparseMatrix(matrix):
        print(f"Matrix ({matrix.rows}x{matrix.cols}):")
        for r in range(matrix.rows):
            row_str = ""
            for c in range(matrix.cols):
                row_str += f"{matrix.getElement(r, c)}\t"
            print(row_str)
        

if __name__ == "__main__":
        while True:
            print("\nSelect Matrix Operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Exit")

            choice = input("Choose an operation (1-4): ")

            if choice == '4':
                print("Exiting the program")
                break
                
            if choice in ('1', '2', '3'):
                try:
                    file1_path = input("Enter the file path for first sparse matrix: ")
                    matrix1 = SparseMatrix(file1_path)
                    file2_path = input("Enter file path for the second sparse matrix: ")
                    matrix2 = SparseMatrix(file2_path)

                    if choice == '1':
                        result_matrix = SparseMatrix.sparseMatrix_addition(matrix1, matrix2)
                        print("\nAddition Result:")
                        SparseMatrix.display_SparseMatrix(result_matrix)
                    elif choice == '2':
                        result_matrix = SparseMatrix.sparseMatrix_subtraction(matrix1, matrix2)
                        print("\nSubtraction Result:")
                        SparseMatrix.display_SparseMatrix(result_matrix)
                    elif choice == '3':
                        result_matrix = SparseMatrix.sparseMatrix_multiplication(matrix1, matrix2)
                        print("\nMultiplication Result:")
                        SparseMatrix.display_SparseMatrix(result_matrix)
                except FileNotFoundError as e:
                    print(f"Error: {e}")
                except ValueError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            else:
                print("Invalid choice. Please choose from 1 to 4!")




                    


