import re
# Lets create a pattern and extract some information with it
regex = re.compile(r"(\w+) World")
result = regex.search("Hello World is the easiest")
if result:
    # This will print:
    #   0 11
    # for the start and end of the match
    print(result.start(), result.end())

# This will print:
#   Hello
#   Bonjour
# for each of the captured groups that matched
for result in regex.findall("Hello World, Bonjour World World 2 job"):
    print(result)

# This will substitute "World" with "Earth" and print:
#   Hello Earth
print(regex.sub(r"\1 Earth", "Hello World"))
