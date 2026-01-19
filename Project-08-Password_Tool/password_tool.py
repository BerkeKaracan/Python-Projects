import random
import string
def scorer(password):
    counter = 0
    password_score = 0
    directions= []
    if len(password) > 12 :
        password_score += 30
    elif len(password)  > 8 :
        password_score += 15
    else:
        directions.append("The password is too short.")
    check1 = any(i.isdigit() for i in password)
    check2 = any(i.isupper() for i in password)
    check3 = any(i.islower() for i in password)
    check4 = any(i in string.punctuation for i in password)

    points=[check1,check2,check3,check4]

    for i in points:
        if i:
            counter += 1
    score = counter * 10
    password_score += score
    if not points[0]:
        directions.append("Missing any a digit.")
    if not points[1]:
        directions.append("Missing any an uppercase letter.")
    if not points[2]:
        directions.append("Missing any a lowercase letter.")
    if not points[3]:
        directions.append("Missing any a special character.")

    return password_score, directions

def password_tool(length_password = 12):
    characters_pool = string.ascii_letters + string.digits + string.punctuation
    while True :
        a = 0
        random_pass = ""
        while a < length_password:
            rndm = random.choice(characters_pool)
            random_pass += rndm
            a += 1
        k = scorer(random_pass)
        goal_score = 70
        if length_password <= 12:
            goal_score = 55
        if length_password <= 8:
            goal_score = 40
        if k[0] >= goal_score:
            return random_pass
        else:
            continue
while True:
    a = input('''
    ---------------------------------------------------
             🔐 PASSWORD SECURITY TOOLKIT 
    ---------------------------------------------------
    1 - Measure Password Security
    2 - Create a New Strong Password
    Q - Quit
    What do you want to do? :
    ''').upper()
    if a == "1":
        b = input("What is your password? :")
        checking = scorer(b)
        print("RECOMMENDATIONS : ")
        for i in checking[1] :
            c = i
            print(c)
        print(f"Your password score : {checking[0]}")
    elif a == "2":
        d = input("Do you want to specify length? (Y/N) :").upper()
        try:
            if d == "Y":
                what_size = int(input("What size password do you want to use? :"))
                if what_size < 4:
                    print("Warning: Too short! Generating anyway...")
                creator = password_tool(length_password=what_size)
                print(creator)
            else:
                creator2 = password_tool()
                print(creator2)
        except ValueError:
            print("❌ Error: Please enter a valid number!")
    elif a == "Q":
        print("Goodbye! Stay safe. 👋")
        break

    else:
        print("Please enter a valid character!")


