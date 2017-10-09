class ticket_manager:

    def ticket_reader(self):
        enter_number_tt = input("Enter the number of your ticket: ")
        f = open('c:\TT\TT_{}.txt'.format(enter_number_tt), 'r')
        print(f.read())
        f.close()
