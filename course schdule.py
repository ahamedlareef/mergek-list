from collections import deque, defaultdict

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    taken = 0
    
    while queue:
        course = queue.popleft()
        taken += 1
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    return taken == numCoursesvfrom collections import deque, defaultdict

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    taken = 0
    
    while queue:
        course = queue.popleft()
        taken += 1
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    return taken == numCourses



