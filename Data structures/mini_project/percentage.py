def student_record_system():
    n = int(input())
    student_records = {}
    
    for _ in range(n):
        line = input().split()
        name = line[0]
        marks = list(map(float, line[1:]))
        student_records[name] = marks
    
    query_name = input("Enter a name: ")
    
    if query_name in student_records:
        marks_list = student_records[query_name]
        average_marks = sum(marks_list) / len(marks_list)
        
        if average_marks.is_integer():
            print(f"Average percentage mark : {int(average_marks)}")
        else:
            print(f"Average percentage mark : {average_marks:.2f}")

if __name__ == "__main__":
    student_record_system()