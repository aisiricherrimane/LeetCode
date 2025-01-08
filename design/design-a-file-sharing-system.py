class FileSharing:

    def __init__(self, m: int):
        self.available_id = []
        self.max_id = 1
        self.chunk_user = defaultdict(set)
        self.user_chunk = defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        if self.available_id:
            id = heapq.heappop(self.available_id)
        else:
            id = self.max_id
            self.max_id += 1
        for chunk in ownedChunks:
            self.chunk_user[chunk].add(id)
            self.user_chunk[id].add(chunk)
        return id

    def leave(self, userID: int) -> None:
        for chunk in self.user_chunk[userID]:
            self.chunk_user[chunk].remove(userID)
        del self.user_chunk[userID]
        heapq.heappush(self.available_id, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        res = sorted(self.chunk_user[chunkID])
        if self.chunk_user[chunkID]:
            self.chunk_user[chunkID].add(userID)
            self.user_chunk[userID].add(chunkID)
        return res
# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)