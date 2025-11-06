#isaplha() checks if the string is empty or does it only contains characters
isalpha_example1 = ""
isalpha_example2 = "ZexLuciferlovesBaiLu"
isalpha_example3 = "I'm 123"

print(isalpha_example1.isalpha())
print(isalpha_example2.isalpha())
print(isalpha_example3.isalpha())


#isalnum() checks if a string contains character or digits and is empty
isalnum1 = ""
isalnum2 = "ZexLuciferlovesBaiLu"
isalnum3 = "123"

print(isalnum1.isalnum())
print(isalnum2.isalnum())
print(isalnum3.isalnum())


#isdecimal() checks if the string has digits or not
isdecimal1 = ""
isdecimal2 = "ZexLuciferlovesBaiLu"
isdecimal3 = "123"

print(isdecimal1.isdecimal())
print(isdecimal2.isdecimal())
print(isdecimal3.isdecimal())


# upper and lower converts the string in upper and lower case
upper_lower = "Zex Lucifer loves Bai Lu"

print(upper_lower.upper())
print(upper_lower.lower())


#islower() and isupper() checks if the string is in lower or upper
isupper_islower = "Zex Lucifer loves Bai Lu"

print(isupper_islower.isupper())
print(isupper_islower.islower())


#title() prints all first letter of the string in upper case
title = "Zex Lucifer loves Bai Lu"

print(title.title())


#startswith() and endswith() are used check wether or not if the string starts or ends with  asub-string
start_end = "Zex Lucifer loves Bai Lu"

print(start_end.startswith("Zex"))
print(start_end.endswith("zex"))


#replace() it replaces a sub-string with other sub-string
replace = "Zex Lucifer loves Bai Lu"

print(replace.replace("Bai Lu", "Bai Meng Yan"))


#strip() it trims all whitespaces in the string at starting and ending
strip = "     Zex Lucifer loves Bai Lu    "
print(strip.strip())


#join() it joins two strings
join = "ZexLuciferloves"
print(join.join('BaiLu'))


#find() it finds a sub-string
find = "Zex Lucifer loves Bai Lu"
print(find.find("Bai Lu"))


#len() return length of the string
length = "Zex Lucifer loves Bai Lu"
print(len(length))

#in operator
in_operation = "Zex Lucifer loves Bai Lu"
print("Bai Lu" in in_operation)