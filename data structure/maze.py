maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

# 创造一个有四个元素的列表，分别代表着当前节点的上下左右的坐标
dirs = [
    lambda x,y: (x+1,y), #右
    lambda x,y: (x,y+1), #上
    lambda x,y: (x-1,y), #左
    lambda x,y: (x,y-1), #下
]

def maze_path(x1, y1, x2, y2):
    stack = []                          # 创造空栈
    stack.append((x1,y1))               # 输入起点坐标.

    # 空栈时表示当前节点回退到起点，且所有的可能路径都已经走遍
    while len(stack) > 0:
        curNode = stack[-1]
        if curNode == (x2, y2):
            print("找到路径：")
            for i in stack:
                print(i)
            return True

        # 遍历四个方向，如果有没走过的坐标则将坐标压栈，值置为2
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                maze[nextNode[0]][nextNode[1]] = 2
                stack.append(nextNode)
                break
        # 遍历四个方向如果没有可以走的路则出栈，退回之前的节点继续寻找可以走的坐标
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    # 空栈时表示没有路径
    print("没有路径！")
    return False



from collections import deque

def maze_path_queue(x1, y1, x2, y2):
    # 创建当前正在考虑的节点的队列和已经走过的节点关系字典
    queue = deque()
    queue.append((x1,y1,-1))
    path = []
    # 只要有正在考虑的数则表示还没穷尽所有的可能性
    while len(queue) > 0:
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print(path)
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                # 后续节点入队，并记录它是由哪个节点带来的
                queue.append((nextNode[0], nextNode[1], len(path)-1))
                maze[nextNode[0]][nextNode[1]] = 2
    else:
        print("没有路径！")
        return False

def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    realpath.append(curNode[0:2]) #起点
    realpath.reverse()
    for node in realpath:
        print(node)

maze_path_queue(1, 1, 8, 8)