defaultString = "{} {} and {}".format("today", "Tomorrow", "Yesterday")
print(defaultString)
orderedString = "{2} {0} and {1}".format("Yesterday", "Today", "Tomorrow")
print(orderedString)
namedString = "{a} {b} and {c}".format(c="Yesterday", b="Today", a="Tomorrow")
print(namedString)
print(type(namedString))