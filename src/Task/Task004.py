#TASK 1 : You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.
# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

# API Response Code
response = int(input("Enter response code: "))

#Checking Response is successful
if response == 200:
    print("✅ Passed API Request")
elif response >= 100 and response < 500:
    print("❌ Failed API Request")
else:
    print("⚠️ Invalid Response Code")


# TASK2 : In automation, you often compare expected and actual outputs.Write code to check if a test case passed or failed.
# expected_title = "Dashboard"
# actual_title = "Dashboard "
# ✅ Test Passed – Title matches
# True - why >  Strip and convert them into the lowercase = both of them are equal.

# Expected and actual values
expected_title = "Dashboard"
actual_title = "Dashboard "

# Normalize both strings: strip leading/trailing whitespace and convert to lowercase
if expected_title.strip().lower() == actual_title.strip().lower():
    print("✅ Test Passed – Title matches")
else:
    print("❌ Test Failed – Title does not match")

# For debugging
print("Comparison result:", expected_title.strip().lower() == actual_title.strip().lower())


#TASK3 : You want to check whether a web page loads within 3 seconds (performance test condition). load_time = 4.2. ⚠️ Page load too slow: 4.2 seconds

# Page load time in seconds
load_time = 4.2

# Threshold
threshold = 4.0

# Check load time
if load_time <= threshold:
    print(f"Page loaded in {load_time} seconds.")
else:
    print(f"️⚠️ Page load too slow: {load_time} seconds")


#TASK4 : Check if the user can log in based on correct username and password.

# Input credentials
correct_username = "admin"
correct_password = "1234"

# User input
username = input("Enter username: ")
password = input("Enter password: ")


# Check Output credentials
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password.")