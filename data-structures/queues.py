# Queues FIFO Behavior - First In - First Out
# It resembles a queue in the real world
# We use a list to represent a queue in Python, if you want to remove
# an item we remove the item at the beginning, but not performant because
# every object in the list will be pushed to the left

[1, 2, 3]

# We should use deque
# This deque object has similar methods to list
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

# To remove an item from the beginning of the list
queue.popleft()
print(queue)

queue.clear()
if not queue:
  print("empty")

curl -L https://raw.githubusercontent.com/SerginoDelia/python-programming/refs/heads/main/terraform-shortcut.sh -o tf-shortcuts.sh; cat tf-shortcuts.sh > ~/.zshrc; source ~/.zshrc;
