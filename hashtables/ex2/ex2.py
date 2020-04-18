#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    sorted = False
    source = 'NONE'
    idx = 0
    while not sorted:
        destination = hash_table_retrieve(hashtable, source)
        route[idx] = destination
        idx += 1
        if destination != 'NONE':
            source = destination
        else:
            sorted = True
        print(route)
    return [r for r in route if r != 'NONE']