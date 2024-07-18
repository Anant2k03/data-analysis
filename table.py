from table import table
list=[
    ["stdid","StdName","standard","Age","hindi","english","math","Science","Computer","Total"]
    ["std01", "Ashish Kumar", "10th", 15, 67, 89, 87, 89, 90, 422]    
    ["std02", "Abhishek Kumnar ", "10th", 14, 85, 45, 48, 90, 45, 313]
    ["std03", "Aman", "10th", 15,23, 56, 78, 78, 67, 302]
    ["std04", "Rahul", "10th", 14, 45, 67, 45, 45, 56, 258]
    ["std05", "Ruby", "10th", 13, 89, 67, 89, 93, 65, 403]
    ["std06", "Suman", "10th", 13, 90, 46, 67, 67, 67, 337]
    ["std07", "saurabh", "10th", 15, 45, 23, 34, 45, 34, 181]
    ["std08", "Sumit", "10th", 14, 23, 45, 67, 78, 90, 303]
    ["std09", "kamlesk", "10th", 15, 45, 56, 78, 99, 67, 303]
    ["std10", "Rohan", "10th", 15, 34, 12, 24, 45, 56, 171]
     ]
table = table()
table.field_names = data[0]

for row in data[1:]:
    table.add_row(row)
print(table)