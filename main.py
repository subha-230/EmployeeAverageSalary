import pandas as pd

content = '[{"userId":"rirani","jobTitleName":"Developer","firstName":"Romin","lastName":"Irani","preferredFullName":"Romin Irani","employeeCode":"E1","region":"CA","phoneNumber":"408-1234567","emailAddress":"romin.k.irani@somemail.com","salary":"20,000"},{"userId":"nirani","jobTitleName":"Developer","firstName":"Neil","lastName":"Irani","preferredFullName":"Neil Irani","employeeCode":"E2","region":"CA","phoneNumber":"408-1111111","emailAddress":"neilrirani@somemail.com","salary":"30,000"},{"userId":"thanks","jobTitleName":"Program Directory","firstName":"Tom","lastName":"Hanks","preferredFullName":"Tom Hanks","employeeCode":"E3","region":"CA","phoneNumber":"408-2222222","emailAddress":"tomhanks@somemail.com","salary":"15,000"},{"userId":"catherine","jobTitleName":"ProductOwner","firstName":"Catherine","lastName":"Blank","preferredFullName":"Catherine Blank","employeeCode":"E4","region":"SA","phoneNumber":"408-23333322","emailAddress":"catherine@somemail.com","salary":"45,000"},{"userId":"Ben","jobTitleName":"ProductOwner","firstName":"Ben","lastName":"Geller","preferredFullName":"Ben Geller","employeeCode":"E5","region":"SA","phoneNumber":"402-125867322","emailAddress":"ben@somemail.com","salary":"25,000"},{"userId":"sarah","jobTitleName":"Developer","firstName":"Sarah","lastName":"Poland","preferredFullName":"Sarah Polland","employeeCode":"E6","region":"FA","phoneNumber":"402-125867653","emailAddress":"sarah@somemail.com","salary":"10,000"},{"userId":"james","jobTitleName":"Developer","firstName":"James","lastName":"Waters","preferredFullName":"James Waters","employeeCode":"E7","region":"YA","phoneNumber":"502-1276543653","emailAddress":"james@somemail.com","salary":"20,000"},{"userId":"liam","jobTitleName":"ProductOwner","firstName":"Liam","lastName":"Brass","preferredFullName":"Liam Brass","employeeCode":"E8","region":"SA","phoneNumber":"602-1111117322","emailAddress":"liam@somemail.com","salary":"25,000"},{"userId":"jen","jobTitleName":"ProductOwner","firstName":"Jenifer","lastName":"Fold","preferredFullName":"Jenifer Fold","employeeCode":"E9","region":"YA","phoneNumber":"602-111000074343","emailAddress":"jen@somemail.com","salary":"17,000"},{"userId":"roar","jobTitleName":"ProductOwner","firstName":"Pat","lastName":"Roam","preferredFullName":"Pat Roam","employeeCode":"E10","region":"CA","phoneNumber":"408-1545634511","emailAddress":"roar@somemail.com","salary":"2,000"}]'

sample_data = pd.read_json(content)

sample_data['salary'] = pd.to_numeric(sample_data['salary'].str.replace(",",""))

region_jobTitleName_Salary = sample_data.groupby(['region','jobTitleName'],as_index=False).salary.mean()

with open('report.txt', 'w') as f:
    for i, j in region_jobTitleName_Salary.iterrows():
        f.write("In '"+j['region']+"' region the avarage salary of a '"+j['jobTitleName']+"' is "+"{:,}".format(round(j['salary'])))
        f.write('\n')

        
#Output:
#In 'CA' region the avarage salary of a 'Developer' is 25,000
#In 'CA' region the avarage salary of a 'ProductOwner' is 2,000
#In 'CA' region the avarage salary of a 'Program Directory' is 15,000
#In 'FA' region the avarage salary of a 'Developer' is 10,000
#In 'SA' region the avarage salary of a 'ProductOwner' is 31,667
#In 'YA' region the avarage salary of a 'Developer' is 20,000
#In 'YA' region the avarage salary of a 'ProductOwner' is 17,000
