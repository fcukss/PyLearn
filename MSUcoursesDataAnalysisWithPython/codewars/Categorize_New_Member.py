def open_or_senior(data):
    new_data=[]
    for item in data:
        if item[0]>=55 and item[1]>7:
            new_data.append("Senior")
        else:
            new_data.append("Open")
    return new_data


a= [(16, 23),(73,1),(56, 20),(1, -1)]
print(open_or_senior(a))