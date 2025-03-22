#เกมทายคำศัพท์
#กด Run and Debug ปุ่มที่ 4 (นับจากบนลงล่าง) ที่อยู่ด้านซ้าย, กด Trust แล้วกด Run ที่มุมขวาบน
import random

listOfWords = ["APPLE", "BREAD", "CLOUD", "DANCE", "FLASH", "GRACE", "HAPPY", "JELLY", "PATTY", "SHARE"]

answer = input("Do you want to play game ?") #YES or NO

while(answer == "YES"):
#สุ่มคำศัพท์มา 1 คำจาก listOfWords
    random_sample = random.sample(listOfWords, 1)
    word = random_sample[0]
    chances = 3
    
    while(chances > 0):
        guess = input("Enter your word: ")
        if guess == word:
            print("You win!!")
            break
        else:
            chances = chances - 1
            print("Try again")
    if chances == 0:
        print("You lose")
    answer = input("Do you want to play another game ?")

print("Game over")