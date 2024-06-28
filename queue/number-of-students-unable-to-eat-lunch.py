class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for s in sandwiches:
            if s in students:
                students.remove(s)
            else:
                return len(students)
        return 0

        