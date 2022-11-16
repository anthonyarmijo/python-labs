guest_list = ['Adriana', 'Mom', 'Dad', 'Jackie']
print(f"{guest_list[0]}, you are cordially invited to dinner.")
print(f"{guest_list[1]}, you are cordially invited to dinner.")
print(f"{guest_list[2]}, you are cordially invited to dinner.")
print(f"{guest_list[3]}, you are cordially invited to dinner.")
print("\n ")

print(f"{guest_list[3]}, you are cordially invited to dinner.")
del guest_list[3]
guest_list.insert(3, "James")

print("\n ")
print(f"{guest_list[0]}, you are cordially invited to dinner.")
print(f"{guest_list[1]}, you are cordially invited to dinner.")
print(f"{guest_list[2]}, you are cordially invited to dinner.")
print(f"{guest_list[3]}, you are cordially invited to dinner.")