surname = "tbelishvili"
print(surname.capitalize())   # მხლოდ პირველი
print(surname.upper())   # ყველა


#replace old emenets with new ones
print(surname.replace("s", "S"))

name = "   tornike    "
surname = "  tbelishvili  "


#Strip აშორებს ზედმეტ spaceb-ს
print(name.strip(),surname)


#დავშალოთ წინადადება სიტყვებად შევქმნათ მათგან სია
my_text = "i love georgia"
print(my_text.split())
