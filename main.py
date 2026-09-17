credits_before = 95
major = "Mathematics"
message = input("How many credits are you taking this semester?")
num = int(message)
credits_taken = (credits_before + num)
credits_to_go = (120 - credits_taken)
print(f"My major is {major}, and I have {credits_to_go} credits to go to graduate.")
