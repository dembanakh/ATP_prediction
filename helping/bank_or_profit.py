from openpyxl import load_workbook
import sys

algos = ["SVM", "GradBoost", "AdaBoost", "LogReg", "MLP", "fixedSVM", "fixedMLP", "fixedGrad", "fixedAda", "fixedLog"]

def sum_up(letter, start, end):
    letter_sum = 0
    for i in range(start, end+1, 3):
        letter_sum += float(file[letter+str(i)].value)
    return letter_sum

for alg in algos:
    print(alg)
    file_name = '../testings/testing_'+alg+'.xlsx'
    file_book = load_workbook(file_name)
    file = file_book['Лист1']
    last_row = len(list(file.rows))
    counter = last_row - 6
    while file['B'+str(counter)].value==None:
        counter -= 3

    if file['E'+str(counter)].value==None:
            ### mode == bank
            
            if sys.argv[-1]!="bank_or_profit.py":
                bank = int(sys.argv[-1])
            else:
                print("\nPlease type in the bank!\n")
                raise

            for letter in ['E', 'G', 'I']:
                file[letter+str(last_row)].value = 'Bank='+str(bank)
            if alg not in ['SVM', 'fixedSVM']:
                file['K'+str(last_row)].value = 'Bank='+str(bank)

    else:
        ### mode == profit

        for letter in ['E', 'G', 'I']:
            last_bank = float(file[letter+str(last_row)].value[5:])
            profit = last_bank - 1000
            file[letter+str(last_row)].value = 'Profit='+str(profit)
        if alg not in ['SVM', 'fixedSVM']:
            letter='K'
            last_bank = float(file[letter+str(last_row)].value[5:])
            profit = last_bank - 1000
            file[letter+str(last_row)].value = 'Profit='+str(profit)

    file_book.save(file_name)
