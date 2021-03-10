from ball import Balls

def juggle(ball1, ball2, ball3):
    ball1.catch()
    ball2.catch()
    ball3.toss()



bk = Balls('Basketball')
bs = Balls('Baseball')
ten = Balls('Tenis')

# avoid accessing private values directly
#bk._is_Moving = True

#we dont need the self here, bc the bk is the instance, so is takinf the self. 
bk.toss()


juggle(bk, bs, ten)
print(bk, bs, ten)
#output: Basketball is in your hand. Baseball is in your hand. Tenis is moving, better catch it

