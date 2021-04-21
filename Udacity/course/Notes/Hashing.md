When we're talking about hash tables, we can define a "load factor":

<b>Load Factor = Number of Entries / Number of Buckets</b>

The purpose of a load factor is to give us a sense of how "full" a hash table is. For example, if we're trying to store 10 values in a hash table with 1000 buckets, 
the load factor would be 0.01, and the majority of buckets in the table will be empty. We end up wasting memory by having so many empty buckets, so we may want to rehash, 
or come up with a new hash function with less buckets. We can use our load factor as an indicator for when to rehash—as the load factor approaches 0, the more empty, 
or sparse, our hash table is.

On the flip side, the closer our load factor is to 1 (meaning the number of values equals the number of buckets), the better it would be for us to rehash and add more buckets. 
Any table with a load value greater than 1 is guaranteed to have collisions.
