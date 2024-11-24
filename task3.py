# Для класса Triangle сделать контроль создания,
# значения должны быть положительны
# и треугольник должен существовать,
# иначе вызвать ошибку ValueError.

class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def valid_triangle(self):
        if (
            self.side_1 + self.side_2 <= self.side_3 or
            self.side_1 + self.side_3 <= self.side_2 or
            self.side_3 + self.side_2 <= self.side_1
        ):
            raise ValueError('Никаки не полусяеся, Насяльнике')
        return 'Можно попробовать'


triangle = Triangle(3, 4, 5)
print(triangle.valid_triangle())
