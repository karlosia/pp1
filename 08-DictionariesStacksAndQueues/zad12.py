student={
    "Name":"John",
    "Age":17,
    "Grade aritmetic mean":4.5,
    "Promoted to graduate":True,
    "Email":{"school":"john@email.com","private":"john.private@gmail.com"}
    
}

import json

with open('studentdata.json','w') as file:
    json.dump(student,file,indent=2)