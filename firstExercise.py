with open('/content/drive/MyDrive/Colab Notebooks/exFolder/students.txt', 'r') as file:
    lines = file.readlines()  # Read all lines into a list
    studentName = "Shay" # @param {"type":"string","placeholder":"Enter name of a student from the group"}

while True:
    if not studentName:  # If no name entered, terminate
        print("No input, terminating program")
        break
        
    found = False
    for i, line in enumerate(lines):
        # Check if the student name is in this line (case-insensitive)
        if studentName.lower() in line.lower():
            print("Student found! Here are their details:")
            print(line.strip())  # strip() removes any trailing newlines
            
            favoriteTVShow = "How I met your mother" # @param {"type":"string","placeholder":"Enter name of favoriteTVShow for a student"}
            
            # Check if favorite TV show already exists
            if "Favorite TV show is:" in line:
                # Split the line at "Favorite TV show is:" and keep the first part
                base_info = line.split("Favorite TV show is:")[0]
                # Create new line with updated TV show
                lines[i] = base_info + f"Favorite TV show is: {favoriteTVShow}\n"
            else:
                # Add TV show for the first time
                lines[i] = line.strip() + f" Favorite TV show is: {favoriteTVShow}\n"
            
            # Save changes to file
            with open('/content/drive/MyDrive/Colab Notebooks/exFolder/students.txt', 'w') as file:
                file.writelines(lines)
                
            print("Updated information:")
            print(lines[i].strip())
            found = True
            break
    
    if not found:
        print("Student name not found, try again")
    
    break  # Exit the loop after one search