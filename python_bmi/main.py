import math

def start_localization():
    print("Choose language: \n1. English\n2. Russian")

    get_choose = int(input())

    if get_choose == 1:
        open_file = "eng"
    elif get_choose == 2:
        open_file = "rus"

    file = open(open_file, "r", encoding = "utf-8")

    #get file size in lines
    j = 0
    for i in file:
        j += 1

    file.close()
    
    text_array = input_array = [0] * j

    file = open(open_file, "r", encoding = "utf-8") #fix

    for x in range(j):
        text_array[x] = file.readline()
    
    file.close()

    check_bmi(text_array, input_array)

def check_bmi(text_array_, input_array_):

    for i in range(len(text_array_) - 8):
        print(text_array_[i][0:len(text_array_[i]) - 1]) #splice for delete \n
        input_array_[i] = input()
    get_index = (float(input_array_[1]) / (math.pow(float(input_array_[2]), 2))) * 10000

    print(input_array_[0] + text_array_[3] + format(get_index, '.2f'))

    if get_index < 16:
        print(text_array_[4])
    elif get_index > 16 and get_index < 18.5:
        print(text_array_[5])
    elif get_index > 18.6 and get_index < 25:
        print(text_array_[6])
    elif get_index > 25.1 and get_index < 30:
        print(text_array_[7])
    elif get_index > 30.1 and get_index < 35:
        print(text_array_[8])
    elif get_index > 35.1 and get_index < 40:
        print(text_array_[9])
    elif get_index > 40.1:
        print(text_array_[10])

if __name__ == '__main__':
    text_array = list()
    input_array = list()
    start_localization()