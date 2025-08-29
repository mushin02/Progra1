def number_sum(number_list):
    total=0
    for number in number_list:
        total+= number
    return total    

def main():
    number_list=[50,100,200]
    total = number_sum(number_list)  
    print(total)      

main()