raw_log = "ERROR_LOG|||  User connection failed   |||IP:192.168.1.1"

# 1. Find the index dynamically
ip_index = raw_log.find("IP:")

# 2. Slice dynamically. We add 3 to skip the "IP:" characters and just get the numbers.
extracted_ip = raw_log[ip_index + 3:]
print(f"Extracted IP: {extracted_ip}")

# 3. Clean the spaces and assign to a variable BEFORE printing
clean_log = raw_log.replace("  ", " ")

# 4. Print using escape sequence formatting (\n for newline, \t for tab)
print(f"Cleaned Log:\n\t{clean_log}")

# 5. Slicing the first 9 characters ("ERROR_LOG") and reversing them with [::-1]
reversed_word = raw_log[0:9][::-1]
print(f"Reversed Word: {reversed_word}")