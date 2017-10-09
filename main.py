from ticket_manager import ticket_manager
from ticket_form import ticket_form

command = input('Enter the command:\n1 - to create a Ticket\n2 - to find the Ticket\n')

if command == '1':
    usr_nm = input('Enter your name: ') + '\n'
    ttl = input('Enter the subject of the request: ') + '\n'
    bdy = input('Describe your problem: ') + '\n'
    ticket_w = ticket_form(ttl, bdy, usr_nm)
    ticket_w.form()

elif command == '2':
    ticket_r = ticket_manager()
    ticket_r.ticket_reader()

else:
    print('Wrong command, try again')

#------------------
# ticket_w = ticket(1, 2, 3)
# ticket_w.count()