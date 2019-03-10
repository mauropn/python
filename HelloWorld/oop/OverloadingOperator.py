class Qualquer:
    def __init__(self, q1, q2):
        self.q1 = q1
        self.q2 = q2

    def __add__(self, other):  # Overloading Operator +
        q1 = self.q1 + other.q1
        q2 = self.q2 + other.q2

        s3 = Qualquer(q1, q2)

        return s3

    def __str__(self):
        return '{} {}'.format(self.q1, self.q2)


q1 = Qualquer(2, 2)
q2 = Qualquer(4, 4)

s3 = q1 + q2

print(s3.q1)

a = 9
print(a)
print(q1)

Qualquer.__str__(q1)
