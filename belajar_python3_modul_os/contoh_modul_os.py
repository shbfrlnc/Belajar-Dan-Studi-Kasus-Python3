import os

print(os.name)
print(os.getcwd())
print(os.path.abspath('.'))
print(os.listdir('.'))

if os.path.isfile("sample.txt") :
    os.rename("sample.txt","renamed.txt")
elif os.path.isfile("renamed.txt") :
    os.rename("renamed.txt","sample.txt")