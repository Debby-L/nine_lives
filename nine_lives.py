import random

lives = 9
words = ['pizza', 'ramen', 'pasta', 'shirt', 'plane', 'teeth']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'  #輸入unicode(萬國碼)表示愛心
guessed_word_correctly = False #玩家不知道答案先用變數值設定false

def update_clue(guessed_letter, secret_word, clue):
	index = 0
	while index < len(secret_word): 
	#len()會回傳指定單字有幾個字母
		if guessed_letter == secret_word[index]:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
		   clue[index] =guessed_letter
		   index = index + 1
		 #如果玩家猜的字母正確，程式會利用變數index找線索清單正確的位置把該位置換成猜對的字母  

while lives > 0: #只要玩家還有生命迴圈會繼續執行
	print(clue) #顯示線索
	print('lives left: ' + heart_symbol * lives)
	guess = input('Guess a letter or the whole word: ') 
    #繼續猜
	if  guess == secret_word:
		guessed_word_correctly = True
		break

	if guess in secret_word:
	   update_clue(guess, secret_word, clue)
	#假如玩家猜中其中一個字母，程式會更新線索
	else:
		print('Incorrect. You lose a life')
		lives = lives - 1
if guessed_word_correctly:
	print('You won! The secret word was ' + secret_word)
else:
	print('You lost! The secret word was ' + secret_word)
	