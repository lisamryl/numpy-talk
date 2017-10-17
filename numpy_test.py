import numpy

A = numpy.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]]).astype(float)
B = numpy.array([6, -4, 27]).astype(float)
A_inverse = numpy.linalg.inv(A)
X = A_inverse.dot(B)

print "Example of System of Equations:"
print "{}x + {}y + {}z = {}".format(A[0][0], A[0][1], A[0][2], B[0])
print "{}x + {}y + {}z = {}".format(A[1][0], A[1][1], A[1][2], B[1])
print "{}x + {}y + {}z = {}".format(A[2][0], A[2][1], A[2][2], B[2])
print "Coefficients Matrix (A):\n{}".format(A)
print "Variables (X): x, y, z"
print "Solutions Vector (B):\n{}".format(B)
print "Answer (Solve for x)\n{}".format(X)
