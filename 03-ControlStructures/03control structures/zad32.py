computer_science = bool(input("Are you interested in computer science? (Y/N): ").upper() == 'Y')
computer_games = bool(input("Do you like playing computer games? (Y/N): ").upper() == 'Y')
instagram_account = bool(input("Do you have an Instagram account? (Y/N): ").upper() == 'Y')

print("\nSurvey Results:")
print("Interested in computer science:", "Yes" if computer_science else "No")
print("Playing computer games:", "Yes" if computer_games else "No")
print("Has an Instagram account:", "Yes" if instagram_account else "No")