#input email of user
# slice the name from the input email

email = input ("enter your email id  :  ")

userName = email[:email.index("@"):].strip()

restName = email[email.index("@")+1::].strip()


g = restName.index(".")
s = email.index("@")+1

domainName = email[s:g+s:].strip()

print('username = {}, domainname = {}'.format(userName,domainName))

