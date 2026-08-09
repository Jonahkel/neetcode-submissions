import bisect

class MapEntry:
    def __init__(self):
        self.entries = []
        self.times = []

class TimeMap:

    def __init__(self):
        self.mapping: dict[str, MapEntry] = defaultdict(MapEntry)


    def set(self, key: str, value: str, timestamp: int) -> None:
        map_entry = self.mapping[key]
        map_entry.entries.append(value) 
        map_entry.times.append(timestamp)


        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        map_entry = self.mapping[key]
        time_idx = bisect.bisect_right(map_entry.times, timestamp)
        if time_idx == 0:
            return ""
        else:
            return map_entry.entries[time_idx-1]
        
