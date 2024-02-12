# Dictionary.
""" A dictionary is a collection while is unorderd, changeable and indexed.
    In python dictionaries are written with curly brakets, and they have
    keys and values."""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year":  "1964",
    "company": "Ford"
    }

print ("The result of print (thisdict) is");
print (thisdict);
print (" ");

x = thisdict["model"]
print ("The result of print(x) is: ");
print (x);
print (" ");

x = thisdict.get("brand")
print ("The result of print(x) is: ");
print (x);
print (" ");

thisdict["year"] = 2018
print ("The result of print (thisdict) after chanfe is: ");
print (thisdict);
print (" ");

print ("The result using 'in' keyword and for loop is: ");
for x in thisdict:
    print (x);
    print (" ");

print ("The result using values method and foe loop");
for x in thisdict.values():
    print (x);
    print (" ");
    
print ("The result when you display key and values");
for x in thisdict.items():
    print (x, y);
    print (" ");

print ("The result when you use len()");
print (len(thisdict));
print (" ");

print ("The result after adding a new item");
thisdict["color"] = "red"
print (thisdict);
print (" ");

print ("The result after deleting an item");
del thisdict["model"]
print (thisdict);
print (" ");

print ("The result after deleting using pop method");
thisdict.pop("year")
print (thisdict);
print (" ");

print ("The result after deleting using pop method");
thisdict.popitem("year")
print (thisdict);
print (" ");

#print ("The result after deleting the dictionary itself");
#del thisdict
#print (thisdict); # This will case an error b/c "thislist" no longer exists.
#print (" ");

thisdict2 = dict (brand='Ford', model='Mustang', year='1964')
# note that keywords are not String literals.
# note the use of equals rather than colon for the assignment.
print (thisdict2);



