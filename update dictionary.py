a={"name":"kavi",
   "age":45,
   "location":"chennai",
   "students":{"karthi","siva"}
    }
a["age"]=50
print(a)


# OR

a={"name":"kavi",
   "age":45,
   "location":"chennai",
   "students":{"karthi","siva"}
    }
a.update({"age": 43})
print(a)
