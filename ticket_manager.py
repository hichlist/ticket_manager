class ticket_manager:

    def __init__(self, ticket_id):
        self.ticket_id = ticket_id

    def ticket_reader(self):
        import sqlite3
        conn = sqlite3.connect("ticket_manager.sqlite")
        cursor = conn.cursor()
        ticket = cursor.execute("select * from Tickets where id_ticket='{}'".format(self.ticket_id))
        conn.commit()
        conn.close()
        return ticket
