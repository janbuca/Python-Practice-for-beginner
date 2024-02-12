# The Set.
""" A set is a collection while undered and unindexed.
In paython sets are writtrn with curly brackets."""

print ("\tThe Set.\n");
thisset = {"apple", "banana", "cherry"}
print (thisset);
print (" ");

print ("The result of print(x) is:");
for x in thisset:
    print (x);

print ("The result of print(x in thisset)");
print ("banana" in thisset);      # Check if "Banana" prsent in the set.
print (" ");

thisset.add("orange")
print ("The result of print(thisset) after adding is:");
print (thisset);
print (" ");

# Add multiple items to a set, using the update() method.
thisset.update(["orange", "mango", "grapes"])
print ("The result of print(thisset) after adding multiple items is:");
print (thisset);
print (" ");

# Get the numbers of items in a set.
print ("The result of print(len(thisset)) is:");
print (len(thisset));
print (" ");

# Remove "banana" by using the remove() method.
thisset.remove("banana")
print ("The result of print(thisset) after removing an item.");
print (thisset);
print (" ");

# Remove "banana" by using the discard() method.
thisset.discard("banana")
print ("The result of print(thisset) after discard an item.");
print (thisset);
print (" ");

# using pop method we can remove the last element.
x = thisset.pop()
print ("The result of print(thisset) after popping off an item.");
print (x);
print (thisset);
print (" ");

# Clearing the content of the set.
thisset.clear()
print ("The result of print(thisset) after Clearing it's content.");
print (thisset);
print (" ");

# del keyword deletes the whole set itself.
""" del thisset
print ("The result of print(thisset) after deleting the set.");
print (thisset); """
print ("\n\n");

# The Set tehoriy.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print ("The result of print (A|B):");
print (A | B);
print (" ");

print ("The result of print (A.union(B)):");
print (A.union(A));
print (" ");

print ("The result of print (B.union(A)):");
print (B.union(A));
print (" ");

print ("The result of print (A&B):");
print (A & B);
print (" ");

print ("The result of print (A.intersection(B)):");
print (A.intersection(B));
print (" ");

print ("The result of print (B.intersection(A)):");
print (B.intersection(A));
print (" ");

print ("The result of print (A-B)");
print (A-B);
print (" ");

print ("The result of print (B-A)");
print (B-A);
print (" ");

print ("The result of print (A.difference(B))");
print (A.difference(B));
print (" ");

print ("The result of print (B.difference(A))");
print (A.difference(B));
print (" ");

print ("The result of print(B^A)");
print (B^A);
print (" ");

print ("The result of print(A.symmetric_difference(B))");
print (A.symmetric_difference(B));
print (" ");

print ("The result of print(B.symmetric_difference(A))");
print (B.symmetric_difference(A));
print ("\n\n");


A1 = {'a', 'c', 'g', 'd'}
B1 = {'c', 'f', 'g' 'h'}
result1 = A1.difference_update(B1)

print ('A1 =', A1);
print ('B1 =', B1);
print ('result1 =', result1);
print (" ");

A2 = {'a', 'c', 'g', 'd'}
B2 = {'c', 'f', 'g' 'h'}


result2 = B2.difference_update(A2)

print ('A2 =', A2);
print ('B2 =', B2);
print ('result2 =', result2);
print (" ");

A3 = {1, 2, 3, 4}
B3 = {2, 3, 4, 5}

result3 = A3.difference_update(B3)

print ('A3 =', A3);
print ('B3 =', B3);
print ('result3 =', result3);
print (" ");

A4 = {1, 2, 3, 4}
B4 = {2, 3, 4, 5, 6}
C4 = {4, 5, 6, 9, 10}

result4 = C4.difference_update(B4, A4)

print ('result3 =', result4);
print ('C4 =', C4);
print ('B4 =', B4);
print ('A4 =', A4);
print (" ");

A5 = {1, 2, 3, 4}
B5 = {5, 6, 7}
C5 = {4, 5, 6}

print ('Are A5 and B5 disjoint', A5.isdisjoint(B5));
print ('Are A5 and C5 disjoint', A5.isdisjoint(C5));
print (" ");

A6 = {1, 2, 3}
B6 = {1, 2, 3, 4, 5}
C6 = {1, 2, 4, 5}

# Returns True.
print (A6.issubset(B6));

# Returns False.
# B6 is not Subset of A6
print (B6.issubset(A6));

# Returns False.
print (A6.issubset(C6)); 

# Returns True.
print (C6.issubset(B6));

A7 = {1, 2, 3, 4, 5}
B7 = {1, 2, 3}
C7 = {1, 2, 3}

# Returns True.
print (A7.issuperset(B7));

# Returns False.
print (B7.issuperset(A7));

# Returns True.
print (C7.issuperset(B7));

# Returns False.
print (B7.issuperset(C7));

A8 = {'a', 'c', 'd'}
B8 = {'c', 'd', 'e'}

result8 = A8.symmetric_difference_update(B8)
print ('A8 =', A8);
print ('B8 =', B8);
print ('result8 =', result8);
print (" ");









