class ticket_form():
    
    def __init__(self, title, body, user_name):
        self.title = title
        self.body = body
        self.user_name = user_name

    def _count(self):
        import os
        import re
        files = os.listdir("c:\TT")
        list_of_tt = ' '.join(files)
        list_of_numbers = (re.findall(r'\d+', list_of_tt))
        max_number = max(list_of_numbers)
        return int(max_number) + 1

    def form(self):
        import random
        deco_line = '________________________________________________________________\n'
        next_number = ticket_form._count(self)
        title_field = self.title
        body_field = self.body
        user_name_field = self.user_name
        ticket_file = open('c:\TT\TT_{}.txt'.format(next_number), 'a')
        ticket_file.write(deco_line)        #Outline
        ticket_file.write(user_name_field)
        ticket_file.write(deco_line)        #Outline
        ticket_file.write(title_field)
        ticket_file.write(deco_line)        #Outline
        ticket_file.write(body_field)
        ticket_file.write(deco_line)        #Outline
        ticket_file.close()
        print('Your Tiket has been created. The number of you Ticket is', next_number)

    # def ticket(self):
    #     enter_number_tt = input("Enter the number of your ticket: ")
    #     f = open('c:\TT\TT_{}.txt'.format(enter_number_tt), 'r')
    #     print(f.read())
    #     f.close()

# usr_nm = input('Enter your name: ') + '\n'
# ttl = input('Enter the subject of the request: ') + '\n'
# bdy = input('Describe your problem: ') + '\n'
#
# ticket_w = ticket(ttl, bdy, usr_nm)
# ticket_w.form()