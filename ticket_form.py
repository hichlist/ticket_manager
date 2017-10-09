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

    def create_ticket(self):
        import sqlite3
        conn = sqlite3.connect("ticket_manager.sqlite")
        cursor = conn.cursor()
        cursor.execute("insert into Tickets ('ticket_title', 'ticket_body', 'user_id') values ('{1}', '{1}', 2)".format(self.title, self.body))
        conn.commit()
        conn.close()
