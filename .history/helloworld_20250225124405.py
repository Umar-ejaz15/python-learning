# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)

# print(txt1)
# print(txt2)
# print(txt3)

# txt ="hellooo"
# print(txt[2:4])
# a= " h "


print(bool("abc"))
print(bool(0))
print(bool(["apple", "cherry", "banana"]))
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))