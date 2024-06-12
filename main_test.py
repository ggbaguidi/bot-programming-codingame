"""test each main module feature"""
from main import Point


x, y, a, b, d, alpha, x_prime, y_prime = 12666, 7656, 5653, 2596, 8648, 0, 13204, 6812

X = Point(in_x=x, in_y=y)
A = Point(in_x=a, in_y=b)
_X = Point(in_x=x_prime, in_y=y_prime)

if __name__ == "__main__":
    print("X:", X)
    print("A:", A)
    print("X - A:", X - A)
    print("D:", _X.dist(A))
    print("angle:", X.degree(_X))
