def convert(num):
    lista = []
    num = str(num).upper().replace(" ", "").replace("0x", "")   
    for i in range(len(num)):
        if num[i] == "A":
            lista.append(10 * 16**i)
        elif num[i] == "B":
            lista.append(11 * 16**i)
        elif num[i] == "C":
            lista.append(12 * 16**i)
        elif num[i] == "D":
            lista.append(13 * 16**i)
        elif num[i] == "E":
            lista.append(14 * 16**i)
        elif num[i] == "F":
            lista.append(15 * 16**i)
        else:
            lista.append(int(num[i]) * 16**i)
    return sum(lista)        

def in_hexa(num):
    if type(num) == float:
        print("Warning: Converting float to int.")
        num = int(num)
    if type(num) == str:
        try:
            num = int(num)
        except:
            pass
    if num == 0:
        return "0"
    
    hexa = ""
    hex_chars = "0123456789ABCDEF"
    
    while num > 0:
        resto = num % 16
        hexa = hex_chars[resto] + hexa
        num //= 16
    return hexa

class hexa:
    def __init__(self, json_data, debug=False):
        self.debug = debug
        self.json_data = json_data
        print("Hexa class initialized with JSON data.")
        if self.debug:
            print("Debug mode is ON.")
            print("JSON data:", self.json_data)
        for key, value in self.json_data.items():
            converted_value = convert(value)
            setattr(self, key, converted_value)
            if self.debug:
                print(f"Key: {key}, Value: {value}")
                
                
    def __repr__(self):
        return f"Class: {self.__class__.__name__}, Hexa: ({self.json_data})"
    
    def __add__(self, other):
        converted_self = convert(self.json_data)
        converted_other = convert(other.json_data)
        return converted_self + converted_other

if __name__ == "__main__":
    print("compilation successful")
    print("This module is not meant to be run directly.")