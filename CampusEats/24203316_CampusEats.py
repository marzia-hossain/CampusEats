#Task 1:
def linear_search(orders,Order_ID):
    for i in range(0,len(orders)):
        if orders[i]["order_id"]==Order_ID:
            return orders[i]
    return "Order not found"

def binary_search(orders,Order_ID):
    left=0
    right=len(orders)-1
    while left<=right:
        middle=(left+right)//2
        if orders[middle]["order_id"]==Order_ID:
            return orders[middle]
        elif orders[middle]["order_id"]>Order_ID:
            right=middle-1
        elif orders[middle]["order_id"]<Order_ID:
            left=middle+1
    if left>right:
        return "Order not found"

#Task 2:
def merge_sort(orders):
    if len(orders)>1:
        left=orders[:len(orders)//2]
        right=orders[len(orders)//2:]
        merge_sort(left)
        merge_sort(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]["priority"]>right[j]["priority"]:
                orders[k]=left[i]
                i+=1
            else:
                orders[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            orders[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            orders[k]=right[j]
            j+=1
            k+=1
    return orders
def top_k_merge_sort(orders,k):
    copied_orders=orders.copy()
    sorted_orders=merge_sort(copied_orders)
    return sorted_orders[:k]

def quickSelect(orders,low,high,k):
    if low==high:
        return orders[low]
    p=partition(orders,low,high)
    if p==k:
        return orders[p]
    elif k<p:
        return quickSelect(orders,low,p-1,k)
    else:
        return quickSelect(orders,p+1,high,k)
def partition(orders,low,high):
    pivot=orders[high]["priority"]
    i=low-1
    for j in range(low,high):
        if orders[j]["priority"]>=pivot:
            i+=1
            orders[i],orders[j]=orders[j],orders[i]
    orders[i+1],orders[high]=orders[high],orders[i+1]
    return i+1
def top_k_quickSelect(orders,k):
    if k<1 or k>len(orders):
        return []
    copied_orders=orders.copy()
    quickSelect(copied_orders,0,len(copied_orders)-1,k-1)
    return copied_orders[:k]


#Task 3:
def sort_intervals_by_finish_time(intervals):
    intervals=sorted(intervals,key=lambda i:i[1])
    return intervals
def interval_scheduling(intervals):
    intervals=sort_intervals_by_finish_time(intervals)
    selected=[]
    if len(intervals)==0:
        return selected
    selected.append(intervals[0])
    finish=intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0]>=finish:
            selected.append(intervals[i])
            finish=intervals[i][1]
    return selected


#Task 4:
def bfs(graph,start):
    if start not in graph:
        return []
    queue=[]
    visited=[]
    queue.append(start)
    visited.append(start)
    while len(queue)>0:
        x=queue.pop(0)
        for i in graph[x]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return visited

def dfs(graph,start):
    if start not in graph:
        return []
    visited=[]
    traversal_order=[]
    return dfs_helper(graph,start,visited,traversal_order)
def dfs_helper(graph,vertex,visited,traversal_order):
    if vertex not in visited:
        visited.append(vertex)
        traversal_order.append(vertex)
        for i in graph[vertex]:
            if i not in visited:
                dfs_helper(graph,i,visited,traversal_order)
    return traversal_order

def dijkstra(graph,source,destination):
    distance={}
    previous={}
    visited=[]
    for vertex in graph:
        distance[vertex]=float("inf")
        previous[vertex]=None
    if source not in graph or destination not in graph:
        return [],float("inf")
    distance[source]=0
    for i in range(len(graph)):
        current=None
        smallest=float("inf")
        for vertex in graph:
            if vertex not in visited and distance[vertex]<smallest:
                smallest=distance[vertex]
                current=vertex
        if current is None:
            break
        visited.append(current)
        for neighbor,weight in graph[current]:
            new_distance=distance[current]+weight
            if new_distance<distance[neighbor]:
                distance[neighbor]=new_distance
                previous[neighbor]=current
    path=[]
    current=destination
    while current is not None:
        path.append(current)
        current=previous[current]
    path.reverse()
    if distance[destination]==float("inf"):
        return[],float("inf")
    return path,distance[destination]

def topological_sort_dfs(graph):
    visited=[]
    stack=[]
    for vertex in graph:
        if vertex not in visited:
            topological_sort_dfs_helper(graph,vertex,visited,stack)
    stack.reverse()
    return stack
def topological_sort_dfs_helper(graph,vertex,visited,stack):
    visited.append(vertex)
    for i in graph[vertex]:
        if i not in visited:
            topological_sort_dfs_helper(graph,i,visited,stack)
    stack.append(vertex)
    return stack


#Task 5:
def knapsack(food_items,budget):
    n=len(food_items)
    dp=[]
    for i in range(n+1):
        row=[]
        for j in range(budget+1):
            row.append(0)
        dp.append(row)
    for i in range(1,n+1):
        price=food_items[i-1]["price"]
        satisfaction=food_items[i-1]["satisfaction"]
        for j in range(budget+1):
            if price>j:
                dp[i][j]=dp[i-1][j]
            else:
                select_item=satisfaction+dp[i-1][j-price]
                skip_item=dp[i-1][j]
                if select_item>skip_item:
                    dp[i][j]=select_item
                else:
                    dp[i][j]=skip_item
    selected_items=[]
    j=budget
    for i in range(n,0,-1):
        if dp[i][j]!=dp[i-1][j]:
            selected_items.append(food_items[i-1])
            j=j-food_items[i-1]["price"]
    selected_items.reverse()
    return selected_items,dp[n][budget]

#Main Function:
def main():
    orders=[
        {
            "order_id":101,
            "student":"Alice",
            "food":"Burger",
            "status":"Delivered" 
        },
        {
            "order_id":102,
            "student":"Bob",
            "food":"Pizza",
            "status":"Preparing"
        },
        {
            "order_id":103,
            "student":"Charlie",
            "food":"Pasta",
            "status":"Pending"
        },
        {
            "order_id":104,
            "student":"David",
            "food":"Sandwich",
            "status":"Delivered"
        }
    ]
    print("Task 1: Student Order Lookup")
    print("Linear Search-Successful:",linear_search(orders,102))
    print("Linear Search-Unsuccessful:",linear_search(orders,110))
    print("Binary Search-Successful:",binary_search(orders,103))
    print("Binary Search-Unsuccessful:",binary_search(orders,115))

    priority_orders = [
        {
            "order_id":201,
            "student":"Sara",
            "priority":70
        },
        {
            "order_id":202,
            "student":"John",
            "priority":95
        },
        {
            "order_id":203,
            "student":"Mina",
            "priority":60
        },
        {
            "order_id":204,
            "student":"David",
            "priority":85
        },
        {
            "order_id":205,
            "student":"Nadia",
            "priority": 90
        }
    ]
    k = 3
    print("\nTask 2: Flash Delivery Prioritization")
    result = top_k_merge_sort(priority_orders, k)
    print("Top-k using Merge Sort:",result)
    result = top_k_quickSelect(priority_orders, k)
    print("Top-k using QuickSelect:",result)

    shifts = [(9, 11),(8, 10),(11, 12),(10, 13),(12, 14),(14, 16),(13, 15)
    ]
    print("\nTask 3: Courier Shift Scheduling")
    selected_shifts = interval_scheduling(shifts)
    print("Selected non-overlapping shifts:")
    for shift in selected_shifts:
        print(shift)

    campus_graph ={
        "Food Court":["Library","Cafeteria"],
        "Library":["Food Court","Lab"],
        "Cafeteria":["Food Court","Lab"],
        "Lab":["Library","Cafeteria","Dormitory"],
        "Dormitory":["Lab"]
    }
    print("\nTask 4: Campus Navigation and Delivery Planning")
    bfs_result = bfs(campus_graph, "Food Court")
    print("BFS Traversal from Food Court:",bfs_result)
    if "Dormitory" in bfs_result:
        print("Dormitory is reachable from Food Court")
    else:
        print("Dormitory is not reachable from Food Court")
    dfs_result = dfs(campus_graph, "Food Court")
    print("DFS Traversal from Food Court:",dfs_result)

    weighted_graph={
        "Food Court":[("Library",4),("Cafeteria",2)],
        "Library":[("Food Court",4),("Lab",3)],
        "Cafeteria":[("Food Court",2),("Lab",5)],
        "Lab":[("Library",3),("Cafeteria",5),("Dormitory",2)],
        "Dormitory":[("Lab",2)]
    }
    shortest_path,shortest_distance=dijkstra(weighted_graph,"Food Court","Dormitory")
    print("Dijkstra Shortest Path:",shortest_path)
    print("Shortest Distance:", shortest_distance)

    task_graph = {
        "Collect Ingredients":["Prepare Food"],
        "Prepare Food":["Pack Order"],
        "Pack Order":["Deliver Order"],
        "Deliver Order":[]
    }
    topological_result = topological_sort_dfs(task_graph)
    print("Topological Sort Task Sequence:",topological_result)

    food_items = [
        {
            "name":"Burger",
            "price":250,
            "satisfaction":80
        },
        {
            "name":"Pizza",
            "price":400,
            "satisfaction":95
        },
        {
            "name":"Pasta",
            "price":300,
            "satisfaction":85
        },
        {
            "name":"Sandwich",
            "price":150,
            "satisfaction":60
        },
        {
            "name":"Juice",
            "price":100,
            "satisfaction":40
        }
    ]
    budget = 700
    print("\nTask 5: Budget-Constrained Meal Package Optimization")
    selected_items,maximum_satisfaction=knapsack(food_items,budget)
    print("Selected Food Items:")
    for item in selected_items:
        print(item["name"])
    print("Maximum Satisfaction:", maximum_satisfaction)

if __name__ == "__main__":
    main()