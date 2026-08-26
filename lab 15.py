# Decision Tree

def decision_tree(age):
    if age < 18:
        return "Not Eligible"
    elif age < 30:
        return "Student"
    elif age < 50:
        return "Working"
    else:
        return "Senior Citizen"

age = int(input("Enter age: "))

result = decision_tree(age)

print("Decision:", result)
