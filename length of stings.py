a = "hello"
freq = {}
for char in a:
    if char in freq:
        freq [char] += 1
    else:
        freq [char] = 1
        
        
print("you entered ",freq)

