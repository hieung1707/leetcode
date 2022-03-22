def solution(num_courses: int, prerequisites: list):
    prerequisite_dict = {}

    for course, prerequisite in prerequisites:
        if course == prerequisite:
            return False

        if prerequisite in prerequisite_dict:
            course_prerequisite = set(prerequisite_dict[prerequisite])

            traversed_prerequisites = []

            while course_prerequisite:
                parent_prerequisites = set()
                for prer in course_prerequisite:
                    if course == prer:
                        return False

                    if prer in prerequisite_dict and prer not in traversed_prerequisites:
                        parent_prerequisites = parent_prerequisites.union(prerequisite_dict[prer])

                    traversed_prerequisites.append(prer)

                course_prerequisite = parent_prerequisites

        if course not in prerequisite_dict:
            prerequisite_dict[course] = []

        prerequisite_dict[course].append(prerequisite)

    return True


def main():
    prerequisites = [[1, 0], [0, 2], [2, 1]]
    num_course = 3

    print(solution(num_course, prerequisites))


if __name__ == "__main__":
    main()
