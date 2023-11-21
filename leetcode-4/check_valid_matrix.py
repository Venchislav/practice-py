def checkValid(matrix):
        vertical_test = 0
        horizontal_test = 0
        matrix = np.array(matrix)

        for i in range(matrix.shape[-1]):
            if sorted(matrix[:,i]) != list(range(1, matrix.shape[1] + 1)):
                return False
            vertical_test += 1

        for i in range(matrix.shape[0]):
            if sorted(matrix[i, :]) != list(range(1, matrix.shape[0] + 1)):
                return False
            horizontal_test += 1

        return (vertical_test == len(matrix)) and (horizontal_test == len(matrix))

        for i in range(matrix.shape[0]):
            if sorted(matrix[:,i]) != list(range(1, len(matrix) + 1)):
                return False
            horizontal_test += 1
        return matrix.shape() == [horizontal_test, vertical_test]



# Too complex, too bad, but it's mine
# GIGACODE
