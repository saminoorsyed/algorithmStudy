# problem description:
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

class TimeMap:

    def __init__(self):
        self.data_struct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data_struct:
            self.data_struct[key].append((value, timestamp))
        else:
            self.data_struct[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data_struct:
            search_list = self.data_struct[key]
            start = 0
            end = len(search_list)-1
            while start <= end:
                middle = (start+ end)//2
                if timestamp == search_list[middle][1]:
                    return search_list[middle][0]
                elif timestamp > search_list[middle][1]:
                    start = middle +1
                else:
                    end = middle-1
            if end>= 0:
                return search_list[end][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ =="__main__":
    obj = TimeMap()
    entries = [["foo", "bar", 1], ["foo", "bar2", 4]]
    obj.set("foo", "bar", 1)
    print(obj.get("foo", 1))
    print(obj.get("foo", 3))
    obj.set("foo", "bar2", 4)
    print(obj.get("foo", 4))
    print(obj.get("foo", 5))

    # output is bar, bar, bar2, bar2 