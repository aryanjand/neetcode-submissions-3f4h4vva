class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        while students and sandwiches:
            j, len_students = 0, len(students)
            while sandwiches[0] != students[0]:
                if j >= len_students:
                    return len_students
                j += 1
                person = students.pop(0)
                students.append(person)
            
            sandwiches.pop(0)
            students.pop(0)
        
        return len(students)