from english_words import get_english_words_set
import string
import random
from colorama import Fore, Style
from datetime import datetime

dic = get_english_words_set(['web2'])

def random_word_generator(num):
    while True:    
        letter = "".join(random.sample(string.ascii_lowercase, num))
        if (letter in dic) == True:
            break
    return letter

def wordle(word):
    print("게임을 시작합니다.")
    life = 0
    abt = list(string.ascii_lowercase)
    out_block = ["※ tried ※"]
    while True:
        life = life+1
        user_input = input('유효한 5자 단어를 입력해주세요: ').lower()
        
        # 5글자 입력이 아닐경우 & 존재하지 않는 단어일 때 무한 질문
        while (len(user_input) != 5) or ((user_input in dic) == False):
            user_input = input('유효하지 않은 단어입니다.\n단어 재입력: ').lower()
        
        answer = []
        inner_block=[]
        for idx, val in enumerate(user_input):
            is_there = word.find(val)
            # 단어안에 해당 글자가 있을 경우
            if is_there != -1:
                # 위치까지 동일하면 초록
                if idx == is_there:
                    char = Fore.GREEN + val + Style.RESET_ALL
                    inner_block.append(Fore.GREEN + "■" + Style.RESET_ALL)
                # 있지만 위치는 다르다면 노랑
                else:
                    char = Fore.YELLOW + val + Style.RESET_ALL
                    inner_block.append(Fore.YELLOW + "■" + Style.RESET_ALL)
                answer.append(char)
            # 단어안에 해당 글자가 아예 없으면 빨강
            elif is_there == -1:
                char = Fore.RED + val + Style.RESET_ALL
                for abt_idx, abt_val in enumerate(abt):
                    if val in abt_val:
                        abt[abt_idx] = char
                answer.append(char)
                inner_block.append("■" + Style.RESET_ALL)
                
        answer = " ".join(answer)
        print(f"\n{ life }번째 시도: { user_input }")  
        print(f"결과: {answer}")
        out_block.append(inner_block)
        print(' '.join(abt))
        
        if answer.count('32') == 5:
            successFlag = True
            print(f'\n축하합니다! {life}번만에 맞추셨습니다!')
            break
        elif life == 6:
            successFlag = False
            print('\n6번의 기회를 모두 사용했지만 정답을 맞추는 것에 실패했습니다.')
            print(f'오늘의 단어는 {word}입니다.')
            break
        
    score = str(input('점수 결과를 공유하시겠습니까? (Y|N)): \n')).upper()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if score == 'Y': 
        for i in out_block:
            for j in i:
                print(j, end='')
            print()
        if successFlag:
            print(f"\n[{now}] {life}번만에 성공했습니다! 축하합니다!")
    else:
        print(f"[{now}] 게임 완료. 수고하셨습니다.")


wordle(random_word_generator(5))