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
        
    def getelement(self, currRow, currCol):
        if not (0 <= currRow < self.rows and 0 <= currCol < self.cols):
            raise IndexError("Row or column index is out of limit!")
        return self.data.get((currRow, currCol), 0)
    
    def setElement(self, currRow, currCol, value):
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

    def sparseMatrix_addition(matrix1, matrix2):
        if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
            raise ValueError("Matrices need to have the same dimensions for addition!")
        result = SparseMatrix(matrix1.rows, matrix1.cols)
        for (r,c), val in matrix1.data.items():
            result.setElement(r, c, val + matrix2.getElement(r, c))
        for (r,c,), val in matrix2.data.items():
            if (r,c) not in result.data:
                result.setElement(r, c, val + matrix1.getElement(r, c))
                return result
            
        


                    


