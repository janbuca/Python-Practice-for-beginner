""" Python Operators.
       1. Aritmetic Operators.
       2. Assigment Operators.
       3. Comparison Operators.
       4. Logical Operators.
       5. Identity Operators.
       6. MemberShip Operators.
       7. Bitwise Operators."""

# 1. Aritmetic Operators.
print ("\tAritmetic Operators.");
x = 50;
y = 25;
z = 3;

c = z + y;
v = x - y;
b = x * y;
n = x / z;
d = y % z;
m = y // z;
a = y ** z;

print ("The Addition of two numbers is       ==>", "" + str(c));
print ("The Subtration of two numbers is     ==>", "" + str(v));
print ("The Multiplication of two numbers is ==>", "" + str(b));
print ("The Division of two numbers is       ==>", "" + str(n));
print ("The Modulus of two numbers is        ==>", "" + str(d));
print ("The Floor division of two numbers is ==>", "" + str(m));
print ("The Exponentiation of two numbers is ==>", "" + str(a));
print ("\n");

# 2. Assignment Operators.
print ("\tAssignment Operators");
a = 5;
a += 5           #a = a + 5.
print ("The value of a += 5 is  ==>", "" + str(a));

b = 9;
b -= 4;         #b = b-4.
print ("The value of b -= 4 is  ==>", "" + str(b));

c = 5;
#c = *= 3;       #c = c*3
print ("The value of c *= 3 is  ==>", "" + str(c));

d = 10;
d /= 5;        #d = d/5..
print ("The value of d /= 5 is  ==>", ""+ str(d));

e = 9;
e %= 2;         #e = e%2.
print ("The value of e %= 2 is  ==>", "" + str(e));

f = 99;
f //= 2;        #f = f//2.
print ("The value of f //= 2 is ==>", "" + str(f));

g = 5;
g **= 3;        #g = g**3.
print ("The value of g **= 3 is ==>", "" + str(g));

h = 5;
h &= 3;        #h = h&3.
print ("The value of h &= 3 is  ==>", "" + str(h));

i = 5;
i |= 3         #i = i|3.
print ("The value of i |= 3 is  ==>", "" + str(i));

j = 5;
j ^=3;        #j = j^3.
print ("THe value of j^=3 is    ==>", "" + str(j));

k = 5;
k >>= 3;      #k = k>>3.
print ("The value of k >>= 3 is ==>", "" + str(k));

l = 5;
l <<= 3       #l = l<<3.
print ("The value of l <<= 3 is ==>", "" + str(l));
print ("\n");

# 3. Comparison Operators.
print ("\tComparison Operators.");
print (5 > 4);
print (5 >= 4);
print (5 < 4);
print (5 <= 4);
print (5 == 4);
print (5 != 4);
print ("\n");

# 4. Logical Operators.
print ("\tLogical Operators.");
print ((5 > 4) or (5 < 4));
print ((5 >= 4) and(5 <= 4));
print (not(5 < 4));
print("\n");

# 5. Identity Operators.
print ("\tIdentity Operators.");
x = ["apple", "banana"];
y = ["apple", "banana"];
z = x;
# returns True b/c z is the same object as x.
print(x is z);
# returns False b/c x is not the same object as y. even if they have the same content.
print(x is y);
# to demonstrate the difference b/n "is" and "==": this compatison returns True b/c x is equal to y.
print(x == y);


