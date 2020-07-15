class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.size = 0

    def __repr__(self):
        return f'key : {self.key},  value : {self.value}'

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        # if self.capacity < MIN_CAPACITY:
        #     self.capacity = MIN_CAPACITY

        self.size = 0
        self.capacity = capacity
        self.hash_table = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

        return self.size / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)

        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        self.size += 1
        old_capacity = self.capacity
        key_index = self.hash_index(key)
        node = self.hash_table[key_index]
        load_factor = self.size / self.capacity
        if node is None:
           self.hash_table[key_index] = HashTableEntry(key, value)
           return
        else:
            current = self.hash_table[key_index]
            prev = current
            while node is not None:
                if current.key == key:
                    print(current, 'current')
                    current.value = value
                    return
                else:
                    prev = node
                    node = node.next
            prev.next = HashTableEntry(key, value)

        if load_factor > 0.7:
            self.resize(self.capacity * 2)
        
        return self.hash_table




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        key_index = self.hash_index(key)
        node = self.hash_table[key_index]
        prev = None

        while node != None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            result = node.value
            if prev is None:
                self.hash_table[key_index] = node.next
            else:
                prev.next = prev.next.next
            return result




    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        key_index = self.hash_index(key)
        node = self.hash_table[key_index]

        while node != None and node.key != key:
            node = node.next 
        if node is None:
            return None
        else: 
            return node.value

        return self.hash_table[key_index]
        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        self.size = 0
        old_table = self.hash_table
        self.hash_table = [None] * new_capacity

        for elem in old_table:
            while elem != None:
                self.put(elem.key, elem.value)
                elem = elem.next
        print(self.hash_table)

    def __str__(self):
        return f'${self.hash_table}'


h = HashTable(9)
n = HashTableEntry('hello', 'world')
h.put('rock', 'Hello World!')
h.put('rock', 'see you soon!')
h.put('rock', 'talk to you later!')
# h.put('kcor', 'goodbye!')
# h.put('kcor', 'ok go')
rock = h.get('rock')
kcor = h.get('kcor')

# print(h.resize(20))
print(rock, 'rock')
# print(kcor, 'kcor')

# if __name__ == "__main__":
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))
