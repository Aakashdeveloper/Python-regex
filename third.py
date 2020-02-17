import re

'''
marks ="123 1234 12345 123456 1234567"
print("matches", len(re.findall("\d{5,7}",marks)))

phone ="412-55575-1212"
if re.search("\d{3}-\d{4}-\d{4}", phone):
    print("Phone number is valid")
else:
    print("Phone number is not valid")


if re.search("\w{2,20}\s\w{2,20}","Aakash handa"):
    print("FullName is valid")
'''

email = "sk@aol.com md2@ab.com xyyz.com a@a a2a@gmail.com"


print("EmailMatches", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,5}",email)))