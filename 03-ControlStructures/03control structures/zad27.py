facebook = bool(input("Does this person have Facebook? Enter true or false: ").lower() == 'true')
instagram = bool(input("Does this person have Instagram? Enter true or false: ").lower() == 'true')
twitter = bool(input("Does this person have Twitter? Enter true or false: ").lower() == 'true')

result = facebook + instagram + twitter

if result >= 2:
    print("This person is a good influencer")
else:
    print("This person is not a good influencer")
