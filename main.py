from ticket_manager import ticket_manager
from ticket_form import ticket_form

command = input('Enter the command:\n1 - to create a Ticket\n2 - to find the Ticket\n')

if command == '1':
    usr_nm = input('Enter your name: ') + '\n'
    ttl = input('Enter the subject of the request: ') + '\n'
    bdy = input('Describe your problem: ') + '\n'
    ticket_w = ticket_form(ttl, bdy, usr_nm)
    # ticket_w.form()
    ticket_w.create_ticket()

elif command == '2':
    ticket_id = input('Enter ticket number: ') + '\n'
    ticket_r = ticket_manager(ticket_id)
    t = ticket_r.ticket_reader()
    r = list(t)
    print(r)

else:
    print('Wrong command, try again')
