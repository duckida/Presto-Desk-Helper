from presto import Presto
from picovector import PicoVector, Polygon, Transform, ANTIALIAS_BEST

presto = Presto()
vector = PicoVector(presto.display)

transform = Transform()
vector.set_transform(transform)

vector.set_antialiasing(ANTIALIAS_BEST)

my_shape = Polygon()


vector.draw(my_shape.rectangle(5, 5, 40, 20, corners=(30, 30, 30, 30), stroke=0))