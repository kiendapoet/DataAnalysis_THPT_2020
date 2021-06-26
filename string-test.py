s = "dunglai"

a = s.split(" ")
print(a)

b = s.replace("lai","x")
print(b)

c= s[5:]
print(c)

upper_case = s.upper()
print(upper_case)

check_upper = s[0].isupper()
print(check_upper)

title_check = s.title()
print(title_check)

swapcase_check = s.swapcase()
print(swapcase_check)

capitalize_check = s.capitalize()
print(capitalize_check)

strip_check = s.strip() # or lstrip or rstrip
print(strip_check)

isdigit_check = s[0].isdigit()
print(isdigit_check)

find_check = s.find("lai")
print (find_check)

index_check = s.index("lai")
print(index_check)

lai_position = s.find("lai")

s1 = s[:lai_position]
s2 = "deptrai"
s3 = s[lai_position:]

s = s1 + s2 + s3
print(s)

print(s.count("a"))