import json
import re

# read JSON file and parse contents
with open('../data/course.json', 'r') as file:
    data = json.load(file) 

jsonl_data = []

for level, courses in data["COIS"].items():
    for code, details in courses.items():
        # Example questions             
                
        jsonl_data.append({
            "prompt": f"What is COIS {code}?",
            "completion": f"COIS {code}- {details['Name']}: {details['Description']}"
        })

        jsonl_data.append({
            "prompt": f"What can you tell me about COIS {code}?",
            "completion": f"COIS {code}- {details['Name']}: {details['Description']}"
        })

        jsonl_data.append({
            "prompt": f"What is {details['Name']}?",
            "completion": f"COIS {code}- {details['Name']}: {details['Description']}"
        })

        jsonl_data.append({
            "prompt": f"What can you tell me about {details['Name']}?",
            "completion": f"COIS {code}- {details['Name']}: {details['Description']}"
        })

        # Location information
        locations = ', '.join(details["Location"])
        locations = re.sub(",", " and ", locations)
        if locations == "Online":
            jsonl_data.append({
                "prompt": f"Where is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered online."
            })

            jsonl_data.append({
                "prompt": f"At what location is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered online."
            })

            jsonl_data.append({
                "prompt": f"Where is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered online."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered Online?",
                "completion": f"Yes, COIS {code} - {details['Name']} is offered online."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered online?",
                "completion": f"Yes, COIS {code} - {details['Name']} is offered online."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered Online?",
                "completion": f"Yes, COIS {code} - {details['Name']} is offered online."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered at any physical locations?",
                "completion": f"No, COIS {code} - {details['Name']} is offered online."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered at any physical locations?",
                "completion": f"No, COIS {code} - {details['Name']} is offered online."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered Peterborough or Durham?",
                "completion": f"No, COIS {code} - {details['Name']} is offered online."
            })

        else:
            jsonl_data.append({
                "prompt": f"Where is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in {locations}."
            })

            jsonl_data.append({
                "prompt": f"At what location is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in {locations}."
            })

            jsonl_data.append({
                "prompt": f"Where is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in {locations}."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered online?",
                "completion": f"No, COIS {code} - {details['Name']} is offered in {locations}."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered online?",
                "completion": f"No, COIS {code} - {details['Name']} is offered in {locations}."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered Online?",
                "completion": f"No, COIS {code} - {details['Name']} is offered in {locations}."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered at any physical locations?",
                "completion": f"Yes, COIS {code} - {details['Name']} is offered in {locations}."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered at any physical locations?",
                "completion": f"Yes, COIS {code} - {details['Name']} is offered in {locations}."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered Peterborough or Durham?",
                "completion": f"Yes, COIS {code} - {details['Name']} is offered in {locations}."
            })

        # Length of program
        length = details["Length"]
        if length == "H":
            jsonl_data.append({
                "prompt": f"How many credits is COIS {code}?",
                "completion": f"COIS {code} - {details['Name']} is for 0.5 credits."
            })

            jsonl_data.append({
                "prompt": f"How many credits is {details['Name']}?",
                "completion": f"COIS {code} - {details['Name']} is for 0.5 credits."
            })

            jsonl_data.append({
                "prompt": f"How many credits do I get after completing {details['Name']}?",
                "completion": f"After completing COIS {code} - {details['Name']} you will get 0.5 credits."
            })

            jsonl_data.append({
                "prompt": f"How many credits do I get after completing COIS {code}?",
                "completion": f"After completing COIS {code} - {details['Name']} you will get 0.5 credits."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} for 0.5 credits?",
                "completion": f"Yes, COIS {code} - {details['Name']} is for 0.5 credits."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} for 0.5 credits?",
                "completion": f"Yes, COIS {code} - {details['Name']} is for 0.5 credits."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} for 1 credits?",
                "completion": f"No, COIS {code} - {details['Name']} is for 0.5 credits."
            })

        elif length == "Y":
            jsonl_data.append({
                "prompt": f"How many credits is COIS {code}?",
                "completion": f"COIS {code} - {details['Name']} is for 1 credits."
            })

            jsonl_data.append({
                "prompt": f"How many credits is {details['Name']}?",
                "completion": f"COIS {code} - {details['Name']} is for 1 credits."
            })

            jsonl_data.append({
                "prompt": f"How many credits do I get after completing {details['Name']}?",
                "completion": f"After completing COIS {code} - {details['Name']} you will get 1 credits."
            })

            jsonl_data.append({
                "prompt": f"How many credits do I get after completing COIS {code}?",
                "completion": f"After completing COIS {code} - {details['Name']} you will get 1 credits."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} for 1 credits?",
                "completion": f"Yes, COIS {code} - {details['Name']} is for 1 credits."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} for 1 credits?",
                "completion": f"Yes, COIS {code} - {details['Name']} is for 1 credits."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} for 0.5 credits?",
                "completion": f"No, COIS {code} - {details['Name']} is for 1 credits."
            })

        # Terms being offered in
        term = details["Term"]
        if term == None:
            jsonl_data.append({
                "prompt": f"What semester is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is not being offered this year."
            })

            jsonl_data.append({
                "prompt": f"What semester is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is not being offered this year."
            })

            jsonl_data.append({
                "prompt": f"In which semester is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is not being offered this year."
            })

            jsonl_data.append({
                "prompt": f"In which semester is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is not being offered this year."
            })

            jsonl_data.append({
                "prompt": f"When is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is not being offered this year."
            })

            jsonl_data.append({
                "prompt": f"When is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is not being offered this year."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered during the Fall semester?",
                "completion": f"No, COIS {code} - {details['Name']} is not being offered this year."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered during the Fall semester?",
                "completion": f"No, COIS {code} - {details['Name']} is not being offered this year."
            })  

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered during the Winter semester?",
                "completion": f"No, COIS {code} - {details['Name']} is not being offered this year."
            })   

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered during the Winter semester?",
                "completion": f"No, COIS {code} - {details['Name']} is not being offered this year."
            })

        elif len(term) == 2:
            jsonl_data.append({
                "prompt": f"What semester is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in both the Fall and Winter semesters."
            })

            jsonl_data.append({
                "prompt": f"What semester is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in both the Fall and Winter semesters."
            })

            jsonl_data.append({
                "prompt": f"In which semester is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in both the Fall and Winter semesters."
            })

            jsonl_data.append({
                "prompt": f"In which semester is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in both the Fall and Winter semesters."
            })

            jsonl_data.append({
                "prompt": f"When is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in both the Fall and Winter semesters."
            })

            jsonl_data.append({
                "prompt": f"When is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in both the Fall and Winter semesters."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered during the Fall semester?",
                "completion": f"Yes, COIS {code} - {details['Name']} is being offered in the Fall semester."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered during the Fall semester?",
                "completion": f"Yes, COIS {code} - {details['Name']} is being offered in the Fall semester."
            })  

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered during the Winter semester?",
                "completion": f"Yes, COIS {code} - {details['Name']} is being offered in the Winter semester."
            })   

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered during the Winter semester?",
                "completion": f"Yes, COIS {code} - {details['Name']} is being offered in the Winter semester."
            })

        elif term[0] == "WI":
            jsonl_data.append({
                "prompt": f"What semester is COIS {code} offered?",
                "completion": f"COIS {code} is offered in the Winter semester."
            })

            jsonl_data.append({
                "prompt": f"What semester is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in only Winter semester."
            })

            jsonl_data.append({
                "prompt": f"In which semester is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in only Winter semester."
            })

            jsonl_data.append({
                "prompt": f"In which semester is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in only Winter semester."
            })

            jsonl_data.append({
                "prompt": f"When is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in only Winter semester."
            })

            jsonl_data.append({
                "prompt": f"When is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in only Winter semester."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered during the Fall semester?",
                "completion": f"No, COIS {code} - {details['Name']} is not being offered in the Fall semester."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered during the Fall semester?",
                "completion": f"No, COIS {code} - {details['Name']} is not being offered in the Fall semester."
            })  

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered during the Winter semester?",
                "completion": f"Yes, COIS {code} - {details['Name']} is being offered in the Winter semester."
            })   

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered during the Winter semester?",
                "completion": f"Yes, COIS {code} - {details['Name']} is being offered in the Winter semester."
            })

        elif term[0] == "FA":
            jsonl_data.append({
                "prompt": f"What semester is COIS {code} offered?",
                "completion": f"COIS {code} is offered in the Fall semester."
            })

            jsonl_data.append({
                "prompt": f"What semester is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in only Fall semester."
            })

            jsonl_data.append({
                "prompt": f"In which semester is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in only Fall semester."
            })

            jsonl_data.append({
                "prompt": f"In which semester is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in only Fall semester."
            })

            jsonl_data.append({
                "prompt": f"When is COIS {code} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in only Fall semester."
            })

            jsonl_data.append({
                "prompt": f"When is {details['Name']} offered?",
                "completion": f"COIS {code} - {details['Name']} is offered in only Fall semester."
            })

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered during the Fall semester?",
                "completion": f"Yes, COIS {code} - {details['Name']} is being offered in the Fall semester."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered during the Fall semester?",
                "completion": f"Yes, COIS {code} - {details['Name']} is being offered in the Fall semester."
            })  

            jsonl_data.append({
                "prompt": f"Is COIS {code} offered during the Winter semester?",
                "completion": f"No, COIS {code} - {details['Name']} is not being offered in the Winter semester."
            })   

            jsonl_data.append({
                "prompt": f"Is {details['Name']} offered during the Winter semester?",
                "completion": f"No, COIS {code} - {details['Name']} is not being offered in the Winter semester."
            })

        # Recommended courses 
        recommended = details["Recommended"]
        if recommended == None:
            jsonl_data.append({
                "prompt": f"What is the recommended course for COIS {code}?",
                "completion": f"No recommended course/courses for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"What is the recommended course for {details['Name']}?",
                "completion": f"No recommended course/courses for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"Are there any recommended courses for COIS {code}?",
                "completion": f"No recommended course/courses for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"Are there any recommended courses for {details['Name']}?",
                "completion": f"No recommended course/courses for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"Is there a recommended course for COIS {code}?",
                "completion": f"No recommended course/courses for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"Is there a recommended course for {details['Name']}?",
                "completion": f"No recommended course/courses for COIS {code} - {details['Name']}."
            })

        else:
            recommended = ', '.join(details["Recommended"])
            jsonl_data.append({
                "prompt": f"What is the recommended course for COIS {code}?",
                "completion": f"The recommended course/courses for COIS {code} - {details['Name']} is/are {recommended}."
            })

            jsonl_data.append({
                "prompt": f"What is the recommended course for {details['Name']}?",
                "completion": f"The recommended course/courses for COIS {code} - {details['Name']} is/are {recommended}."
            })

            jsonl_data.append({
                "prompt": f"Are there any recommended courses for COIS {code}?",
                "completion": f"Yes, The recommended course/courses for COIS {code} - {details['Name']} is/are {recommended}."
            })

            jsonl_data.append({
                "prompt": f"Are there any recommended courses for {details['Name']}?",
                "completion": f"Yes, The recommended course/courses for COIS {code}  - {details['Name']} is/are {recommended}."
            })

            jsonl_data.append({
                "prompt": f"Is there a recommended course for COIS {code}?",
                "completion": f"Yes, The recommended course/courses for COIS {code} - {details['Name']} is/are {recommended}."
            })

            jsonl_data.append({
                "prompt": f"Is there a recommended course for {details['Name']}?",
                "completion": f"Yes, The recommended course/courses for COIS {code} - {details['Name']} is/are {recommended}."
            })

        # Any co-requisites required
        coReq = details["Co-requisites"]
        if coReq == None:
            jsonl_data.append({
                "prompt": f"What are the Co-requisites courses for COIS {code}?",
                "completion": f"No Co-requisites course/courses for COIS {code} - {details['Name']} ."
            })

            jsonl_data.append({
                "prompt": f"What are the Co-requisites courses for {details['Name']}?",
                "completion": f"No Co-requisites course/courses for COIS {code} - {details['Name']} ."
            })

            jsonl_data.append({
                "prompt": f"Are there any Co-requisites courses for COIS {code}?",
                "completion": f"No Co-requisites course/courses for COIS {code} - {details['Name']} ."
            })

            jsonl_data.append({
                "prompt": f"Are there any Co-requisites courses for {details['Name']}?",
                "completion": f"No Co-requisites course/courses for COIS {code} - {details['Name']} ."
            })

            jsonl_data.append({
                "prompt": f"Is there a Co-requisite course for COIS {code}?",
                "completion": f"No Co-requisites course/courses for COIS {code} - {details['Name']} ."
            })

            jsonl_data.append({
                "prompt": f"Is there a Co-requisite course for {details['Name']}?",
                "completion": f"No Co-requisites course/courses for COIS {code} - {details['Name']} ."
            })
        else:
            coReq = ', '.join(details["Co-requisites"])
            jsonl_data.append({
                "prompt": f"What is the Co-requisites course for COIS {code}?",
                "completion": f"The Co-requisites course/courses for COIS {code} - {details['Name']}  is/are {coReq}."
            })

            jsonl_data.append({
                "prompt": f"What are the Co-requisites courses for {details['Name']}?",
                "completion": f"The Co-requisites course/courses for COIS {code} - {details['Name']}  is/are {coReq}."
            })

            jsonl_data.append({
                "prompt": f"Are there any Co-requisites courses for COIS {code}?",
                "completion": f"Yes, the Co-requisites course/courses for COIS {code} - {details['Name']}  is/are {coReq}."
            })

            jsonl_data.append({
                "prompt": f"Are there any Co-requisites courses for {details['Name']}?",
                "completion": f"Yes, the Co-requisites course/courses for COIS {code} - {details['Name']}  is/are {coReq}."
            })

            jsonl_data.append({
                "prompt": f"Is there a Co-requisite course for COIS {code}?",
                "completion": f"Yes, the Co-requisites course/courses for COIS {code} - {details['Name']}  is/are {coReq}."
            })

            jsonl_data.append({
                "prompt": f"Is there a Co-requisite course for {details['Name']}?",
                "completion": f"Yes, the Co-requisites course/courses for COIS {code} - {details['Name']}  is/are {coReq}."
            })

        # Is the course cross-listed with any other course in another department?
        crossListed = details["Cross-Listed"]
        if crossListed == None:
            jsonl_data.append({
                "prompt": f"Is COIS {code} cross-listed with any other course?",
                "completion": f"No, COIS {code} - {details['Name']} is not cross-listed with any other courses ."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} cross-listed with any other course?",
                "completion": f"No, COIS {code} - {details['Name']} is not cross-listed with any other courses ."
            })

            jsonl_data.append({
                "prompt": f"What course is cross-listed with {details['Name']}?",
                "completion": f"COIS {code} - {details['Name']} is not cross-listed with any other courses ."
            })

            jsonl_data.append({
                "prompt": f"What course is cross-listed with COIS {code}?",
                "completion": f"COIS {code} - {details['Name']} is not cross-listed with any other courses ."
            })

            jsonl_data.append({
                "prompt": f"Is  any course cross-listed with {details['Name']}?",
                "completion": f"No, COIS {code} - {details['Name']} is not cross-listed with any other courses ."
            })

            jsonl_data.append({
                "prompt": f"Is any course cross-listed with COIS {code}?",
                "completion": f"No, COIS {code} - {details['Name']} is not cross-listed with any other courses ."
            })

            jsonl_data.append({
                "prompt": f"Tell me the course that is cross-listed with COIS {code}?",
                "completion": f"COIS {code} - {details['Name']} is not cross-listed with any other courses ."
            })

            jsonl_data.append({
                "prompt": f"Tell me the course that is cross-listed with {details['Name']}?",
                "completion": f"COIS {code} - {details['Name']} is not cross-listed with any other courses ."
            })

        else:
            crossListed = ', '.join(details["Cross-Listed"])
            crossListed = re.sub(",", " and ", crossListed)
            jsonl_data.append({
                "prompt": f"Is COIS {code} cross-listed with any other course?",
                "completion": f"Yes, COIS {code} - {details['Name']} is cross-listed with {crossListed}."
            })

            jsonl_data.append({
                "prompt": f"Is {details['Name']} cross-listed with any other course?",
                "completion": f"Yes, COIS {code} - {details['Name']} is cross-listed with {crossListed}."
            })

            jsonl_data.append({
                "prompt": f"What course is cross-listed with {details['Name']}?",
                "completion": f"COIS {code} - {details['Name']} is cross-listed with {crossListed}."
            })

            jsonl_data.append({
                "prompt": f"What course is cross-listed with COIS {code}?",
                "completion": f"Yes, COIS {code} - {details['Name']} is cross-listed with {crossListed}."
            })

            jsonl_data.append({
                "prompt": f"Is  any course cross-listed with {details['Name']}?",
                "completion": f"Yes, COIS {code} - {details['Name']} is cross-listed with {crossListed}."
            })

            jsonl_data.append({
                "prompt": f"Is any course cross-listed with COIS {code}?",
                "completion": f"Yes, COIS {code} - {details['Name']} is cross-listed with {crossListed}."
            })

            jsonl_data.append({
                "prompt": f"Tell me the course that is cross-listed with COIS {code}?",
                "completion": f"COIS {code} - {details['Name']} is cross-listed with {crossListed}."
            })

            jsonl_data.append({
                "prompt": f"Tell me the course that is cross-listed with {details['Name']}?",
                "completion": f"COIS {code} - {details['Name']} is cross-listed with {crossListed}."
            })

        # Are there any restrcition on who can take the course
        restrictions = details["Restrictions"]
        if restrictions == None:
            jsonl_data.append({
                "prompt": f"What are the restrictions for COIS {code}?",
                "completion": f"No restrictions for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"What are the restrictions for {details['Name']}?",
                "completion": f"No restrictions for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"Are there any restrictions for COIS {code}?",
                "completion": f"No, there are no restrictions for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"Are there any restrictions for {details['Name']}?",
                "completion": f"No, there are no restrictions for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"Tell me the restrictions for COIS {code}?",
                "completion": f"COIS {code} - {details['Name']} has no restrictions."
            })

            jsonl_data.append({
                "prompt": f"Tell me the restrictions for {details['Name']}?",
                "completion": f"COIS {code} - {details['Name']} has no restrictions."
            })
        else:
            jsonl_data.append({
                "prompt": f"What are the restrictions for COIS {code}?",
                "completion": f"Restrictions for COIS {code} - {details['Name']} is {restrictions}."
            })

            jsonl_data.append({
                "prompt": f"What are the restrictions for {details['Name']}?",
                "completion": f"Restrictions for COIS {code} - {details['Name']} is {restrictions}."
            })

            jsonl_data.append({
                "prompt": f"Are there any restrictions for COIS {code}?",
                "completion": f"Yes, the restrictions for COIS {code} - {details['Name']} is {restrictions}."
            })

            jsonl_data.append({
                "prompt": f"Are there any restrictions for {details['Name']}?",
                "completion": f"Yes, the restrictions for COIS {code} - {details['Name']} is {restrictions}."
            })

            jsonl_data.append({
                "prompt": f"Tell me the restrictions for COIS {code}?",
                "completion": f"Restrictions for COIS {code} - {details['Name']} is {restrictions}."
            })

            jsonl_data.append({
                "prompt": f"Tell me the restrictions for {details['Name']}?",
                "completion": f"Restrictions for COIS {code} - {details['Name']} is {restrictions}."
            })

        # Are there any pre-requisites courses that need to completed before taking this course
        prereqs = details["Pre-requisites"]
        if prereqs == None:
            jsonl_data.append({
                "prompt": f"What are the prerequisites for COIS {code}?",
                "completion": f"No prerequisites for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"What are the prerequisites for {details['Name']}?",
                "completion": f"No prerequisites for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"Are there any prerequisites for COIS {code}?",
                "completion": f"No, there are no prerequisites for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"Are there any prerequisites for {details['Name']}?",
                "completion": f"No, there are no prerequisites for COIS {code} - {details['Name']}."
            })

            jsonl_data.append({
                "prompt": f"Tell me the prerequisites for COIS {code}?",
                "completion": f"COIS {code} - {details['Name']} has no prerequisites."
            })

            jsonl_data.append({
                "prompt": f"Tell me the prerequisites for {details['Name']}?",
                "completion": f"COIS {code} - {details['Name']} has no prerequisites."
            })

            jsonl_data.append({
                    "prompt": f"Does COIS {code} have any prerequisites?",
                    "completion": f"No, there are no prerequisites for COIS {code} - {details['Name']}."
                })

            jsonl_data.append({
                "prompt": f"Does {details['Name']} have any prerequisites?",
                "completion": f"No, there are no prerequisites for COIS {code} - {details['Name']}."
            })
        else:
            prereq = details["Pre-requisites"][0]
            if prereq["Requirement"] == "Single prerequisite" and prereq["Courses"] is not None:
                course = prereq["Courses"][0]
                jsonl_data.append({
                        "prompt": f"What is the prerequisite for COIS {code}?",
                        "completion": f"The prerequisite for COIS {code} - {details['Name']} is {course}."
                    })
                
                jsonl_data.append({
                    "prompt": f"What are the prerequisites for {details['Name']}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} is {course}."
                })

                jsonl_data.append({
                    "prompt": f"Are there any prerequisites for COIS {code}?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} is {course}."
                })

                jsonl_data.append({
                    "prompt": f"Are there any prerequisites for {details['Name']}?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} is {course}."
                })

                jsonl_data.append({
                    "prompt": f"Tell me the prerequisites for COIS {code}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} is {course}."
                })

                jsonl_data.append({
                    "prompt": f"Tell me the prerequisites for {details['Name']}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} is {course}."
                })

                jsonl_data.append({
                    "prompt": f"Does COIS {code} have any prerequisites?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} is {course}."
                })

                jsonl_data.append({
                    "prompt": f"Does {details['Name']} have any prerequisites?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} is {course}."
                })

            elif prereq["Requirement"] == "Single prerequisite":
                credits = prereq["Credits"][0]
                jsonl_data.append({
                        "prompt": f"What is the prerequisite for COIS {code}?",
                        "completion": f"The prerequisite for COIS {code} - {details['Name']} is {credits}."
                    })
                
                jsonl_data.append({
                    "prompt": f"What are the prerequisites for {details['Name']}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} is {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Are there any prerequisites for COIS {code}?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} is {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Are there any prerequisites for {details['Name']}?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} is {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Tell me the prerequisites for COIS {code}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} is {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Tell me the prerequisites for {details['Name']}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} is {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Does COIS {code} have any prerequisites?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} is {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Does {details['Name']} have any prerequisites?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} is {credits}."
                })


            elif prereq["Requirement"] == "Alternative prerequisites with credits":
                courses = " or ".join(course for course in prereq["Courses"])
                credits = prereq["Credits"]
                jsonl_data.append({
                    "prompt": f"What is the prerequisite for COIS {code}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses} or {credits}."
                })

                jsonl_data.append({
                    "prompt": f"What are the prerequisites for {details['Name']}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses} or {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Are there any prerequisites for COIS {code}?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses} or {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Are there any prerequisites for {details['Name']}?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses} or {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Tell me the prerequisites for COIS {code}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses} or {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Tell me the prerequisites for {details['Name']}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses} or {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Does COIS {code} have any prerequisites?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses} or {credits}."
                })

                jsonl_data.append({
                    "prompt": f"Does {details['Name']} have any prerequisites?",
                    "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses} or {credits}."
                })

            elif prereq["Requirement"] == "Alternative prerequisites":
                if all(isinstance(course, str) for course in prereq["Courses"]):
                    courses = " or ".join(course for course in prereq["Courses"])
                    jsonl_data.append({
                        "prompt": f"What is the prerequisite for COIS {code}?",
                        "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                    "prompt": f"What are the prerequisites for {details['Name']}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for COIS {code}?",
                        "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for {details['Name']}?",
                        "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for COIS {code}?",
                        "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does COIS {code} have any prerequisites?",
                        "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does {details['Name']} have any prerequisites?",
                        "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                else:
                    courses = ", ".join(str(course) for course in prereq["Courses"])
                    courses = re.sub("\[", "", courses)
                    courses = re.sub("'", "", courses)
                    courses = re.sub("\],", " or ", courses)
                    courses = re.sub("\]", "", courses)
                    jsonl_data.append({
                        "prompt": f"What is the prerequisite for COIS {code}?",
                        "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                    "prompt": f"What are the prerequisites for {details['Name']}?",
                    "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for COIS {code}?",
                        "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for {details['Name']}?",
                        "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for COIS {code}?",
                        "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does COIS {code} have any prerequisites?",
                        "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does {details['Name']} have any prerequisites?",
                        "completion": f"Yes, the prerequisite for COIS {code} - {details['Name']} are {courses}."
                    })

            elif prereq["Requirement"] == "Multiple prerequisites":
                courses = ",".join(prereq["Courses"])
                courses = re.sub(",", " and ", courses)
                jsonl_data.append({
                    "prompt": f"What are the prerequisites for COIS {code}?",
                    "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses}."
                })

                jsonl_data.append({
                    "prompt": f"What are the prerequisites for {details['Name']}?",
                    "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses}."
                })

                jsonl_data.append({
                    "prompt": f"Are there any prerequisites for COIS {code}?",
                    "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses}."
                })

                jsonl_data.append({
                    "prompt": f"Are there any prerequisites for {details['Name']}?",
                    "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses}."
                })

                jsonl_data.append({
                    "prompt": f"Tell me the prerequisites for COIS {code}?",
                    "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses}."
                })

                jsonl_data.append({
                    "prompt": f"Tell me the prerequisites for {details['Name']}?",
                    "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses}."
                })

                jsonl_data.append({
                    "prompt": f"Does COIS {code} have any prerequisites?",
                    "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses}."
                })

                jsonl_data.append({
                    "prompt": f"Does {details['Name']} have any prerequisites?",
                    "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses}."
                })
            elif prereq["Requirement"] == "Multiple prerequisites with grade":
                if prereq["Courses"] is not None:
                    courses = ",".join(prereq["Courses"])
                    courses = re.sub(",", " and ", courses)
                    grade = prereq["Grade"]
                    jsonl_data.append({
                        "prompt": f"What are the prerequisites for COIS {code}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"What are the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for COIS {code}?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for {details['Name']}?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for COIS {code}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does COIS {code} have any prerequisites?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does {details['Name']} have any prerequisites?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade}."
                    })
                else:
                    grade = prereq["Grade"]
                    jsonl_data.append({
                        "prompt": f"What are the prerequisites for COIS {code}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} is a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"What are the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} is a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for COIS {code}?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} is a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for {details['Name']}?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} is a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for COIS {code}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} is a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} is a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does COIS {code} have any prerequisites?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} is a grade of {grade}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does {details['Name']} have any prerequisites?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} is a grade of {grade}."
                    })
            elif prereq["Requirement"] == "Multiple prerequisites with credits and grade":
                if prereq["Courses"] is not None:
                    courses = ",".join(prereq["Courses"])
                    courses = re.sub(",", " and ", courses)
                    grade = prereq["Grade"]
                    credits = prereq["Credits"]
                    jsonl_data.append({
                        "prompt": f"What are the prerequisites for COIS {code}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"What are the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for COIS {code}?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for {details['Name']}?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for COIS {code}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does COIS {code} have any prerequisites?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does {details['Name']} have any prerequisites?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and a grade of {grade} and {credits}."
                    })
                elif prereq["Courses"] is None:
                    grade = prereq["Grade"]
                    credits = prereq["Credits"]
                    jsonl_data.append({
                        "prompt": f"What are the prerequisites for COIS {code}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"What are the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for COIS {code}?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for {details['Name']}?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for COIS {code}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does COIS {code} have any prerequisites?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are a grade of {grade} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does {details['Name']} have any prerequisites?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are a grade of {grade} and {credits}."
                    })
            elif prereq["Requirement"] == "Multiple prerequisites with credits":
                if prereq["Courses"] is not None:
                    courses = ", ".join(str(course) for course in prereq["Courses"])
                    courses = re.sub("\[", "", courses)
                    courses = re.sub("'", "", courses)
                    courses = re.sub("\],", " or ", courses)
                    courses = re.sub("\]", "", courses)
                    credits = prereq["Credits"]
                    jsonl_data.append({
                        "prompt": f"What are the prerequisites for COIS {code}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"What are the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for COIS {code}?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Are there any prerequisites for {details['Name']}?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for COIS {code}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Tell me the prerequisites for {details['Name']}?",
                        "completion": f"The prerequisites for COIS {code} - {details['Name']} are {courses} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does COIS {code} have any prerequisites?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and {credits}."
                    })

                    jsonl_data.append({
                        "prompt": f"Does {details['Name']} have any prerequisites?",
                        "completion": f"Yes, the prerequisites for COIS {code} - {details['Name']} are {courses} and {credits}."
                    })

# Save as JSONL
with open("../data/course_data_new.jsonl", "w") as f:
    for entry in jsonl_data:
        f.write(json.dumps(entry) + "\n")
