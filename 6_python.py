# Python String.
print ("\tPython String.");
# n[a:b] 'a' is the position of the beginning and 'b' is the ending
n = "Welcome our home!!!";

print ("The value of n is        =>" + n);
print ("The value of n[1] is     =>" + n[1]);
print ("The value of n[2:5] is   =>" + n[2:5]);
print ("The value of n[5:] is    =>" + n[5:]);
print ("The value of n[:7] is    =>" + n[:7]);
print ("The value of n[-4:] is   =>" + n[-4:]);
print ("The value of n[:] is     =>" + n[:]);
print ("The value of n[-5:-2] is =>" + n[-5:-2]);
print ("The value of n[::2] is   =>" + n[::2]);
print ("The value of n[::] is    =>" + n[::]);
print ("\n");

x = "   Ouer, Famile Members is, living in the Ethiopian, countrey.!!! ";
print (x[::]);
print (x);
print (x.strip());
print (len(x));
print (x.lower());
print (x.upper());
print (x.replace("O", "W"));
print (x.split(","));
