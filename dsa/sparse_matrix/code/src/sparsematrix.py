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
            with open(file_path, 'r') as file:
                lines = f.readlines()

                if not lines:
                    raise ValueError("Input file is empty!")
                
                dimension_line = lines[0].strip()
                ports = dimension_line.split(',')
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
                
