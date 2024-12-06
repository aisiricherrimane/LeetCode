from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def time_to_minutes(time: str) -> int:
            # Convert "HH:MM" to total minutes since midnight
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes

        # Step 1: Group times by names
        store = defaultdict(list)
        for i in range(len(keyName)):
            store[keyName[i]].append(time_to_minutes(keyTime[i]))

        # Step 2: Check for alerts
        alert_list = []
        for person in store:
            times = sorted(store[person])  # Sort the times for each person
            for i in range(len(times) - 2):  # Check every group of 3 consecutive times
                if times[i + 2] - times[i] <= 60:  # 1-hour window
                    alert_list.append(person)
                    break  # No need to check further for this person

        # Step 3: Return sorted list of names
        return sorted(alert_list)
