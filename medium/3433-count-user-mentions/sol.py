class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key = lambda x: ( int(x[1]), -ord(x[0][0]) ))
        mentions = [0 for _ in range(numberOfUsers)]
        active = [1 for _ in range(numberOfUsers)]
        heap = []
        allMentions = 0
        # print(events)

        for typ, tmstmp, mentionStr in events:
            t = int(tmstmp)
            # CHECK IF BACK ONLINE ############################################
            while heap and heap[0][0] + 60 <= t:
                _, _id = heapq.heappop(heap)
                active[_id] = 1
            # OFFLINE #########################################################
            if typ == "OFFLINE":
                _id = int(mentionStr) 
                heapq.heappush(heap,(t,_id))
                active[_id] = 0
            # MESSAGE ######################################################
            else:
                if mentionStr == "ALL":  # -----------------------------
                    allMentions += 1
                elif mentionStr == "HERE": # ---------------------------
                    for i in range(numberOfUsers):
                        mentions[i] += active[i]
                else: # ----------------------------------------------
                    for s in mentionStr.split(" "):
                        _id = int(s[2:])
                        mentions[_id] += 1

        if allMentions:
            for i in range(numberOfUsers):
                mentions[i] += allMentions

        return mentions