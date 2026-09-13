Notes

replace(old, new) replaces one string with another.

phone = "98-788-262-845"

clean_phone = phone.replace("-", "")

print(clean_phone)

This is especially useful for data cleaning.


replace()

price='12345,44444'
print(price.replace(',','.'))

phone='98-788-262-845'
print(phone.replace('-',''))

cost='$34,98.545'
print(cost.replace(',','.').replace('.',''))
