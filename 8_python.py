# Python Lists.
# Python Collections (Arrays).

listfirut = ["Mango", "Apple", "Banana", "Zeytun", "Kazimir"]
print (listfirut);             # it return all of the list.
print (listfirut[2]);          # it return index 2 banana from the list.
listfirut[2] = "Boko";
print (listfirut);             # it reples the index 2 banana by boko.
for a in listfirut:
    print(a);                  # display each by induvdualy.
print  (len(listfirut));       # display the length of the word.  
listfirut.append("Carot");
print (listfirut);             # display carot at the end of the list.
listfirut.insert(1, "Mixaxish");  
print (listfirut);             # return mixaxish index 2.
listfirut.remove("Kazimir"); 
print (listfirut);             # removeing Kazimir from the list.
listfirut.pop(0)
print (listfirut);             # removeing the first indes[0] mango.

# del listfirut
# print (listfirut);          # Delete of all displaying list
# listfirut.clear()
# print (listfirut);          # Clear the list

print ("\n\n");


thislist = ["Dog", "Cat", "Croodile", "Goat", "Sheep", "Ape", "Parrot", "Bird",
            "Hen", "Ox", "Caw", "Hose", "Camel", "Donkey", "Monkey"]
print("The value of thislist");
print(thislist);
print ("the value of the thislist [1] is:");
print(thislist[1]);
print ("The value of the thislist [2:5]");
print (thislist[2:5]);
print ("The value of the thislist [5:]");
print (thislist[5:]);
print ("The value of the thislist [:7]");
print (thislist[:7]);
print ("The value of the thislist [-4:]");
print (thislist[-4:]);
print ("The value of the thislist [:]");
print (thislist[:]);
print ("The value of the thislist [-5:-2]");
print (thislist[-5:-2]);
print ("The value of the thislist [::2]");
print (thislist[::2]);
