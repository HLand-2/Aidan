import random

txt1 = ["Cool", "Smart", "Gross", "Big", "Small", "Good", "Bad", "Happy", "Sad", "Tall", "Short"]
txt2 = ["Time", "Person", "Year", "Way", "Day", "Thing", "Man", "World", "Life", "Hand"]

z5 = 1
while 1 == 1:
    t = random.choice(txt1) + random.choice(txt2)
    no = str(random.randint(100, 9999))
    user = t + no
    t3 = "Username: "
    t4 = t3 + user

    Chars = []
    chars = "§1234567890-=±!@£$%^&*()_+€#qwertyuiop   []QWERTYUIOP{}asdfghjkl;'\\ASDFGHJKL:|`zxcvbnm,./~ZXCVBNM<>?"
    c2 = list(chars)
    i = 1
    while i < len(chars):
        Chars.append(chars[i - 1])
        i = i + 1
    chars = Chars
    pswlen = random.randint(8, 32)
    password = ""
    DB = []
    i = 1
    while i < pswlen:
        DB.append(chars[random.randint(0, len(chars) - 1)])
        i = i + 1
    i = 0
    print(len(DB))
    while i < len(DB):
        password = password + DB[i]
        i = i + 1
    print("Combination", str(z5) + ":")
    print("Username:", user)
    print("Password:", password)
    print()
    z5 = z5 + 1
