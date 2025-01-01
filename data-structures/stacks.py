# Stacks - LIFO (Last In - First Out)
# Similar to a browser keeping a stack of the websites you visited
# when you hit the back button, you're redirected to the previous website
# If you keep hitting the back button to the beginning the back button will 
# be disabled

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

# When the user presses the back button we should remove the last item on this list
last = browsing_session.pop()
print(last)
print(browsing_session)

# Return the last item in the stack
print("redirect", browsing_session[-1])

# if the list is empty remove the back button
browsing_session.clear()

if not browsing_session:
  print("disable")
