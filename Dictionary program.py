s={
    "roll_no":101,
    "name":"Amit",
    "marks":85
}
print("Dictionary: ", s)
print("Name: ",s["name"])
print("Marks: ", s.get("marks"))
print()
print("2. Update dictionary")
s["marks"]=90
s["grade"]="A"
print("Updated Dictionary:", s)
print()
print("3. Removing Elements")
removed_value= s.pop("grade")
print("Removed Value:", removed_value)
print("After Removing 'grade': ", s)
s.popitem()
print("After popitem(): ", s)
print()
print("4. Merging dictionaries")
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
merged_dict =dict1|dict2
print("First Dictionary:",dict1)
print("Second Dictionary: ",dict2)
print("Merged Dictionary: ",merged_dict)