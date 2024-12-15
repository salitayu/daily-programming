"""
:type classes: List[List[int]]
:type extraStudents: int
:rtype: float
2d int array class
classes[i] = [passi, totali]
in the ith class, there are a total i total students
but only pass i number of students will pass the exam
classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2
you can assign the two extra students to the first class
output: 0.78333
the average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333
"""
def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Lambda to calculate the gain of adding an extra student
        def _calculate_gain(passes, total_students):
            return (passes + 1) / (total_students + 1) - passes / total_students

        # Max heap to store (-gain, passes, total_students)
        max_heap = []
        for passes, total_students in classes:
            gain = _calculate_gain(passes, total_students)
            heapq.heappush(max_heap, (-gain, passes, total_students))

        # Distribute extra students
        for _ in range(extraStudents):
            current_gain, passes, total_students = heapq.heappop(max_heap)
            heapq.heappush(
                max_heap,
                (
                    -_calculate_gain(passes + 1, total_students + 1),
                    passes + 1,
                    total_students + 1,
                ),
            )

        # Calculate the final average pass ratio
        total_pass_ratio = 0
        while max_heap:
            _, passes, total_students = heapq.heappop(max_heap)
            total_pass_ratio += passes / total_students
        return total_pass_ratio / len(classes)
