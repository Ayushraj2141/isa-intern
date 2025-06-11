from datetime import datetime as dt 
now = dt.now()
user_name = input("Hey user could you please enter your name ")
print(f'''
    Letter to user : 
     Hey, {user_name}
        Hope you are doing good \n \t and this letter finds you in best of your health 
            written on {now.date()} at {now.time()}

      ''')