class Matrix:

    def __init__(self,  _list=[]):
        """
        checking that matrix is right dimension
        (every row has equal length)
        """
        self.is_correct = True
        self._list = _list
        if not _list:
            self.dim_col = 0
            self.dim_row = 0
            self.is_correct = False
        else:
            self.dim_col = len(_list[0])
            self.dim_row = len(_list)

            try:
                for i in range(self.dim_row):
                    if len(_list[i]) != self.dim_col:
                        raise Exception("Matrix dimension ERROR")
                if self.dim_col == 0:
                    raise Exception("Matrix is empty")
            except Exception as ex:
                self.is_correct = False
                print(ex, "\nMatrix can't be built")

    def __str__(self):
        if self.is_correct:
            res = 'Matrix dimension:' + str(self.dim_row) + "x" + str(self.dim_col) + '\n'
            for i in range(self.dim_row):
                res += str(self._list[i]) + '\n'
        else:
            res = 'object is broken and cannot be printed'
        return res

    # Insert method to create nodes
    def __add__(self, other):
        if not self.is_correct or not other.is_correct:
            raise Exception("some matrix is empty")
        elif self.dim_col != other.dim_col or self.dim_row != other.dim_row:
            raise Exception("dimensions do not match")

        # res = Matrix(self._list)
        _tmp_list = []
        for i in range(self.dim_row):
            _tmp_list.append([])
            for j in range(self.dim_col):
                _tmp_list[i].append(0)
        # print(res)

        for i in range(self.dim_row):
            for j in range(self.dim_col):
                _tmp_list[i][j] = self._list[i][j] + other._list[i][j]
        return Matrix(_tmp_list)

    def __mul__(self, other):
        if not self.is_correct or not other.is_correct:
            raise Exception("some matrix is empty")
        elif self.dim_col != other.dim_row :
            raise Exception("dimensions do not match")

        tmp_list = []
        for i in range(self.dim_row):
            tmp_list.append([])
            for j in range(other.dim_col):
                tmp_list[i].append(0)

        res_matrix = Matrix(tmp_list)

        for i in range(self.dim_row):
            for j in range(other.dim_col):
                for k in range(self.dim_col):
                    res_matrix._list[i][j] += self._list[i][k]*other._list[k][j]
        return res_matrix

    def __sub__(self, other):
        if not self.is_correct or not other.is_correct:
            raise Exception("some matrix is empty")
        elif self.dim_col != other.dim_col or self.dim_row != other.dim_row:
            raise Exception("dimensions do not match")

        _tmp_list = []
        for i in range(self.dim_row):
            _tmp_list.append([])
            for j in range(self.dim_col):
                _tmp_list[i].append(0)

        for i in range(self.dim_row):
            for j in range(self.dim_col):
                _tmp_list[i][j] = self._list[i][j] - other._list[i][j]
        return Matrix(_tmp_list)

    def multy_num(self, num):
        if self.is_correct:
            for i in range(self.dim_row):
                for j in range(self.dim_col):
                    self._list[i][j] *= num
        else:
            raise Exception('object is broken and cannot be multyplied by number')
        return self

    def trans(self):
        tmp_list = []
        for i in range(self.dim_col):
            tmp_list.append([])
            for j in range(self.dim_row):
                tmp_list[i].append(self._list[j][i])
        return Matrix(tmp_list)

    def matrix_to_triangeled(self):
        if not self.is_correct:
            raise Exception('Matrix is empty')
        if self.dim_col != self.dim_row:
            raise Exception('Incorrect dimensions')

        _tmp_list = []
        for i in range(self.dim_row):
            _tmp_list.append([])
            for j in range(self.dim_col):
                _tmp_list[i].append(self._list[i][j])

        print("start transforming matrix")
        for i in range(self.dim_row-1):
            if _tmp_list[i][i] == 0:
                for j in range(i+1, self.dim_row):
                    if _tmp_list[j][i] != 0:
                        _tmp_list[i], _tmp_list[j] = _tmp_list[j], _tmp_list[i]
                        break
                if _tmp_list[i][i] == 0:
                    continue
                else:
                    for j in range(i+1, self.dim_row):
                        if _tmp_list[j][i] != 0:
                            alfa = _tmp_list[i][i] / _tmp_list[j][i]
                            for k in range(self.dim_col):
                                _tmp_list[j][k] = _tmp_list[i][k] - _tmp_list[j][k]*alfa
            else:
                for j in range(i + 1, self.dim_row):
                    if _tmp_list[j][i] != 0:
                        alfa = _tmp_list[i][i] / _tmp_list[j][i]
                        for k in range(self.dim_col):
                            _tmp_list[j][k] = _tmp_list[i][k] - _tmp_list[j][k] * alfa

        return Matrix(_tmp_list)


def main():
    a = Matrix([[13, 22], [1, 2], [1, 22]])
    # b = Matrix([[], []])
    c = Matrix([[1, 1], [1, 1], [1, 1]])
    d = Matrix([[1, 2], [1, 2]])

    m = Matrix([[0, 0, 0], [1, 2, 3], [2, 2, 2]])

    print(d)
    # print(b)
    print(a)
    print(c)

    a_c = a + c
    print('ac= ', a_c)
    ab = a + a
    print(a.multy_num(10))

    # matrix multiply:
    q = a * d
    print(q)

    # перевантажені методи віднімання додавання:
    print(a-a)
    print(a+a)
    print(a)

    print('Matrix transponded:')
    print(a)
    b = a.trans()
    print(b)

    print('Matrix to triangeled:')
    print(m)
    print(m.matrix_to_triangeled())


if __name__ == '__main__':
    main()
