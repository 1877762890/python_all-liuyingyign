def  isExists(chose,data):
    if chose in data:
        return True
    return False

def  getRandom():
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range(8):
        string =  string + li[int(random.random()* len(li))]
    return string



def bank_transfer(username,password,account,money):
    if money not in bank[username]["money"]:
        return 3
    elif password not in bank[username]["password"]:
        return 2
    elif account not in  bank[username]["account"]:
        return 1
    else:
        bank_[transfer]={
            "account": getRandom(),
            "password": password,
            "money": money,
        }
    return 0









