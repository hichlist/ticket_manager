from ticket_manager import ticket_manager
from ticket_form import ticket_form

command = input('Enter the command:\n1 - to create a Ticket\n2 - to find the Ticket\n')

if command == '1':
    usr_nm = input('Enter your name: ')
    ttl = input('Enter the subject of the request: ')
    bdy = input('Describe your problem: ')
    ticket_write = ticket_form(ttl, bdy, usr_nm)
    ticket_write.create_ticket()

elif command == '2':
    ticket_id = int(input('Enter ticket number: '))
    ticket_read = ticket_manager(ticket_id)
    t = ticket_read.ticket_reader()

else:
    print('Wrong command, try again')
