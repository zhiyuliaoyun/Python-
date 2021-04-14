def check_card_number(card_num):
      c=[]
      sum=0
      while card_num!=0:
            b=card_num%10
            c.append(b)
            card_num=int(card_num/10)
      card_num_length=len(c)
      for i in range(1, card_num_length + 1):
           t = int(c[card_num_length - i])
           if i % 2 == 0:
                 t *= 2
                 sum += t if t < 10 else t % 10 + t // 10
           else:
                 sum += t
      return sum % 10 == 0
      
      check_card_number ( 5082337440657928 )
      
def check_card_number_str(card_num):
    sum = 0
    card_num_length = len(card_num)
    for i in range(1, card_num_length + 1):
        t = int(card_num[card_num_length - i])
        if i % 2 == 0:
            t *= 2
            sum += t if t < 10 else t % 10 + t // 10
        else:
            sum += t
    return sum % 10 == 0
    
    check_card_number_str('6226095711985771')
    
import random
def generate_card_number(start_with, total_num):
    result = start_with
 
    while len(result) < total_num - 1:
        result += str(random.randint(0, 9))
    s = 0
    card_num_length = len(result)
    for i in range(2, card_num_length + 2):
        t = int(result[card_num_length - i + 1])
        if i % 2 == 0:
            t *= 2
            s += t if t < 10 else t % 10 + t // 10
        else:
            s += t
 
    t = 10 - s % 10
    result += str(0 if t == 10 else t)
    return result
 
if __name__ == '__main__':
    for _ in range(1000):
        new_card_num = generate_card_number('62260', 16)
        valid_result = check_card_number_str(new_card_num)
        print('%s %s' % (new_card_num, valid_result))
