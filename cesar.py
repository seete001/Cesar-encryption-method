alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P","Q", "R", "S", "T", "U", "V","W", "X", "Y", "Z"]
def decode(cipher ):
    for key in range(1, 25):
        res = ""
        for ch in cipher:
            for i in range(len(alpha)):
                if ch == alpha[i]:
                    res += alpha[(i + key)%26]
        print(f"Key : {key} : {res}")

def encode(key, text):
    res = ""
    for ch in text.upper(): 
        for i in range(len(alpha)):
            if alpha[i] == ch:
                res += alpha[(i + key)% 26]
    return res


if __name__ == "__main__":
    op = input("[E]ncode/[D]ecode?")
    if op.upper() == "E":
        text = input("Text : ")
        key = input("Key : ")
        print( encode(int(key) , text) )
    elif op.upper() == "D":
        text = input("Text : ")
        print( decode(text) )

