class SquareRoot():

    def __init__(self, square_to_test):
        '''

        :param square_to_test: integer
        '''

        self.square_to_test = square_to_test

    def test_guess(self):
        if abs(self.guess ** 2 - self.square_to_test ) < 0.001:
            return True
        else:
            return False

    def test_perfect_square(self):
        int_of_guess = int(self.guess)
        if int_of_guess ** 2 == int(self.square_to_test):
            return True

    def approx_sqroot(self):
        self.guess = self.square_to_test / 2
        counter = 1
        while self.test_guess() == False:
            self.guess = (self.guess + (self.square_to_test/self.guess)) / 2
            counter += 1
        self.square_root = self.guess

    def process_square(self):
        self.approx_sqroot()
        if self.test_perfect_square():
            return self.square_root
