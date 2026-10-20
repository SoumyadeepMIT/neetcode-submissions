import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        free = list(range(n))      # min-heap of room numbers
        busy = []                  # min-heap of (end_time, room)
        count = [0] * n

        for start, end in meetings:
            # Rooms that finished by `start` become free
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)

            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
            else:
                # No room free: wait for the earliest one, delay the meeting
                free_at, room = heapq.heappop(busy)
                heapq.heappush(busy, (free_at + (end - start), room))

            count[room] += 1

        return count.index(max(count))   # lowest index wins ties