def main():
    s = str(input("Please enter the sentence: "))
    numWords = len(s.split(" "))
    average = 0
    for n in s:
        average = average + len(n)  
    average = (average - s.count(" "))/numWords   
    print("Number of characters:", len(s))
    print("Number of words:",  numWords)
    print("Average word length:", average)
    
main()
