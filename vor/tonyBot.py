import time
import random
# 定义一个聊天机器父类，用来实现程序提出问题，用户输入，程序输出功能，并且有延时的时间设定
class Bot:
    
    wait = 1
    
    def __init__(self):
        self.q = ''
        self.a = ''
    
    def _think(self,a):
        return a
      
    def run(self):        
        time.sleep(self.wait)
        print(self.q)
        self.a = input()
        self._think(self.a)

class HelloBot(Bot):
    
    def __init__(self,q):
        self.q = q
        
    def _think(self,a):
        print(f'Hello {a} ')

class HowFineBot(Bot):
    
    def __init__(self,q):
        self.q = q
        
    def _think(self,a):
        if 'good' in a.lower() or 'fine' in a.lower():
            print("It's fine Today!") 
        else:
            print("I'm sorry to hear that!") 


class FavorColorBot(Bot):
    
    def __init__(self,q):
        self.q = q
        
    def _think(self,a):
        colors = ['red','green','puple','orange','indigo','yellow'] 
        print(f'Your favourite color is {a},my favourite color is {random.choice(colors)}') 

class TonyTalkBot():
    
    def __init__(self,wait):
        Bot.wait = wait
        self.bots = []
        
    def add(self,bot):
        self.bots.append(bot)
        
    def _prompt(self):
        print("This is tony talkShow,Let's talk")
        print()
        
    def run(self):
        self._prompt()
        for bot in self.bots:
            bot.run()

if __name__ == '__main__':
    tonyTalkBot = TonyTalkBot(1)
    hellobot = HelloBot("What's your name?")
    howFineBot=HowFineBot("how are you？")
    favorColorBot=FavorColorBot("What’s your favourite Color?")
    tonyTalkBot.add(hellobot)
    tonyTalkBot.add(howFineBot)
    tonyTalkBot.add(favorColorBot)
    tonyTalkBot.run()            