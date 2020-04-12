# myinfo = {'Username' : 'asifulmamun',
#             'Name' : 'Al Mamun',
#             'Mobile' : '01721600688'
# }

# print(str(myinfo['Username']))

# for keys, values in myinfo.items():
#     print(keys, values)


users = {
    'mamun' : {
        'Name' : 'Al Mamun',
        'Age' : '22',
        'Dist' : 'Kishoreganj'
    },
    'rafi' : {
        'Name' : 'Rafi',
        'Age' : '23',
        'Dist' : 'Sirajganj'
    }
}

# print(users['mamun']['Age'])

for keys, values in users.items():
    # print(keys)
    # print(values)
    # print(keys, values['Name'], values['Age']) # with specific keys name, age it's values

    for nextkeys, nextvalues in values.items():
        print(nextkeys) # print 1st dictionary keys valus under 2nd dictionary keys
        print(nextvalues) # print 1st dictionary keys valus under 2nd dictionary keys values