sec_in_hour = 3600
sec_in_min = 60

print("Input a raw number of seconds: (eg: 3665)")
input_num = int(input())

hours = input_num // sec_in_hour
remaining_after_hours = input_num % sec_in_hour

minutes = remaining_after_hours // sec_in_min
seconds = remaining_after_hours % sec_in_min

print(f"hours: {hours}, minutes: {minutes}, seconds: {seconds}")
