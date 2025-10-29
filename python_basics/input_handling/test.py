
import sys

full_name=sys.argv[1:]
'''last_name=sys.argv[2]

email=full_name.replace(" ",".")+last_name.replace(" ",".")+"@company.com"

print(f"First_name :{full_name} Last Name : {last_name}")
print(f"email : {email}")'''
name=" ".join(full_name)
print(name)

