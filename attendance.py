total_classes = int(input("enter total number of classes conducted: "))
attended_classes = int(input("enter number of classes attended: "))
min_percentage_input = input("enter minimum required attendance percentage (default is 75): ")

if min_percentage_input.strip() == "":
    min_required = 75
else:
    min_required = float(min_percentage_input)

current_percentage = (attended_classes / total_classes) * 100
print(f"\nyour current attendance is: {current_percentage:.2f}%")

if current_percentage >= min_required:
    missable_classes = 0
    while True:
        future_total = total_classes + missable_classes + 1
        future_attended = attended_classes
        future_percentage = (future_attended / future_total) * 100
        if future_percentage < min_required:
            break
        missable_classes += 1

    print(f"you can miss {missable_classes} more class(es) and still maintain at least {min_required}% attendance.")

else:
    needed_classes = 0
    while True:
        future_total = total_classes + needed_classes + 1
        future_attended = attended_classes + needed_classes + 1
        future_percentage = (future_attended / future_total) * 100
        if future_percentage >= min_required:
            break
        needed_classes += 1

    print(f"you need to attend the next {needed_classes + 1} class(es) without missing to reach at least {min_required}% attendance.")
