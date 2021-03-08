import random

lives = 9
words = ['pizza', 'ramen', 'pasta', 'shirt', 'plane', 'teeth']
secret_word = random.choice(words)
clue = []
index = 0
while index < len(secret_word):
	clue.append('?')
	index = index + 1
heart_symbol = u'\u2764'  #輸入unicode(萬國碼)表示愛心
guessed_word_correctly = False #玩家不知道答案先用變數值設定false
unknown_letters = len(secret_word) #j玩家不知道所有字母

def update_clue(guessed_letter, secret_word, clue, unknown_letters):
	index = 0
	while index < len(secret_word): 
	#len()會回傳指定單字有幾個字母
		if guessed_letter == secret_word[index]:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
		   clue[index] =guessed_letter
		   unknown_letters = unknown_letters - 1 #每當玩家猜對的字母，unknown_letters會-1
		   index = index + 1
		 #如果玩家猜的字母正確，程式會利用變數index找線索清單正確的位置把該位置換成猜對的字母  

	return unknown_letters #讓函式回傳未知字母個數

#區分難度
difficulty = input('Choose difficulty (type 1, 2 or 3):\n 1 Easy\n 2 Normal\n 3 Hard\n')
difficulty = int(difficulty)

#依難度顯示生命值
if difficulty == 1:
	lives = 12
elif difficulty == 2:
	lives = 9
else:
	lives = 6


while lives > 0: #只要玩家還有生命迴圈會繼續執行
	print(clue)  #顯示線索
	print('lives left: ' + heart_symbol * lives)
	guess = input('Guess a letter or the whole word: ') 
    #繼續猜
	if  guess == secret_word:
		guessed_word_correctly = True
		break

	if guess in secret_word:
		unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
	
	else:
		print('Incorrect. You lose a life')
		lives = lives - 1

    if unknown_letters == 0:
    	guessed_word_correctly = True
    	break

