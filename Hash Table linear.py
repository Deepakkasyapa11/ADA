class HashTable:
    
    def __init__(self, m):
        self.m = m
        self.hashtable = self.create_hash_table()
    
    def create_hash_table(self):
        return [ [] for _ in range(self.m) ]
    
    def _prehash(self, key):
        #challenge: handle negative keys and string
        if (type(key) == str):
            key = hash(key)  #returns a number for you
            
        if ((type(key) == int) | (type(key) == float)):
            if (key < 0):
                key = hash(float(key)) * -1  #first convert to float, then hash it
        
        assert (key > 0) & (type(key) == int)
    
        return key
    
    def _hash(self, key):
        #get the position using division method
        index = key % self.m
        bucket = self.hashtable[index]
        return bucket
    def resize_table(self):
        pass
      
    def put(self,val):
        load factor = self.count / len(self.table)
        if load_factor + 1 > 0.66:
           self.resize_table()

        self.count += 1 
        index = self.hash(val) 
        if self.table[index] is None or self.table[index] == val:

           self.table[index] = value 
       else:
           print(Hash collision!)
        
           i = 1 
           done = False 
           while not done:
    
               new_index = (index + i) % len(self.table)
               if new_index == index:
          
                   raise ValError("Hash table is full ! ")
            
               if self.table[new_index] is None or self.table[new_index] == val:
                
                   self.table[new index] = value
                   
                   done = True 
                else:
               
                  i += 1
                
      def get(self, val):
        
         index = self.hash(val)
         if self.table[index] == val or self.table[index] is None:
            return self.table[index] 
         else:
            return "Oops! Value not what I expected!" !

        
        
        
        
    def insert(self, key, val):
        
        key    = self._prehash(key)  #clean neg numbers or string
        bucket = self._hash(key)     #get the position of the hashtable
        
        # found = False
        # #check whether the key duplicates
        # for i, (bkey, bval) in enumerate(bucket):
        #     if bkey == key:
        #         found = True
        #         pos_dup = i
        #         break
        found, pos_dup, _ = self.search(key)
                
        #if the key duplicates, only update the value
        if(found):
            bucket[pos_dup] = (key, val)
        else: #if the key does not exist, append and #if something is there already, append
            bucket.append((key, val))
            
        print(self.hashtable)
    
    def search(self, key):
        #if you finish this, 
        key = self._prehash(key)
        
        #perform the division method
        bucket = self._hash(key)     #get the position of the hashtable

        found  = False
        answer = -9999
        pos_dup = -9999
        #loop the bucket index
        for i, (bkey, bval) in enumerate(bucket):
            if bkey == key:
                found   = True
                pos_dup = i
                answer  = bval
                break
                
        return found, pos_dup, answer  
    
    def delete(self, key):
        
       i = 0
       repeat
        j = ht(self, key)
        if self[j] == key
           self[j] = DELETE
            return j
        else i = i + 1
    until self[j] == NIL or i == m
    error "element not exist"

ht = HashTable(11)
ht.insert(1, 'Chaky')
ht.insert(2, 'Peter')
ht.insert(2, 'Peterss')
ht.insert(3, 'John')
ht.insert(12, 'Matthew')  #this should be in the same bucket with 'Chaky'

found, _, val = ht.search(12)
print(found, val)
