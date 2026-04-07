import re
text = "My phone number is 9876543210 and my email is example@gmail.com"
phone_pattern = r'\d{10}'
email_pattern = r'\S+@\S+'
phone = re.search(phone_pattern, text)
email = re.search(email_pattern, text)
if phone:
    print("Phone Number Found:", phone.group())
if email:
    print("Email Found:", email.group())
