"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

# Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000 # An array with 10k Nones.

    def store(self, string):
        index = self.calculate_hash_value(string)
        if self.table[index] is None:
            self.table[index] = [string]
        else:
            self.table[index].append(string)

    def lookup(self, string):
        index = self.calculate_hash_value(string)
        if self.table[index] != None:
            if string in self.table[index]:
                return index
        return -1

    def calculate_hash_value(self, string):
        return ord(string[0]) * 100 + ord(string[1])
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
