from vector import Vector

class TestVector:

    def test_create(self):
        v =Vector (x=1, y=2)
        assert True

    def test_add(self):
        v1 = Vector(1, 2)
        v2 = Vector(2, 2)
        v3 = Vector (3, 4)

        v= v1 +v2
        assert v.x == 3
        assert  v.y == 4
        assert v == v3

    def test_sub(self):
