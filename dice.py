import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    n = 100000 #number of rolls of d dice
    d = 3 #number of dice in each roll
    rolls = []
    for i in range(n):
        indivRoll = []
        for j in range(d):
            roll = np.random.randint(6) + 1
            indivRoll.append(roll)
        rolls.append(indivRoll)

    sixCount = 0 #counter for number of times that 3 sixes are rolled
    elevenCount = 0 #counter for number of times that a sum of 11 is rolled
    sumList = []
    for i in range(len(rolls)):
        total = sum(rolls[i])
        if total == 18:
            sixCount += 1 
            sumList.append(total)
        elif total == 11:
            elevenCount += 1
            sumList.append(total)
        else:
            sumList.append(total)

    sixProb = sixCount/len(rolls)
    elevenProb = elevenCount/len(rolls)

    print("The probability of rolling all sixes is", sixProb)
    print('The probability of rolling a total of eleven is', elevenProb)

    plt.hist(sumList, bins=16, density=True)
    plt.title('Distribution of Sum of Dice Rolls')
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability Density of Each Sum')
    plt.show()
    
            
            
            
    
