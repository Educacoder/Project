import pandas as pd

while True:
  print("")
  print('*******PSI data analytic System*******')
  print('1. Display PSI reading for 2023 in Singapore')
  print('2. To display the highest PSI reading')
  print('3. To display the lowest PSI reading')
  print('4. To update PSI reading')
  print('5. To Save PSI data file \n')
  print('Press any other numbers to exit')

# Prompt the user to enter an option
  choice = input('Enter your option:')

# Use if - elif for conditional check and match the input (1 to 5, any other number exit the program)
  if choice == '1':
    # read excel file and assign to a data frame pd.read_excel(XXXX.xlsx)

    # Add your codes.....

  elif choice == '2':
    # Prompt user to enter direction north, south, east or west for the highest PSI
    # Display the highest directon PSI. Hint: You may use method max() from pandas

    # Add your codes....

  elif choice == '3':
    # Prompt user to enter direction north, south, east or west for the lowest PSI
    # Display the lowest directon PSI. Hint: You may use method min() from pandas

    # Add your codes....

  elif choice == '4':
    # Prompt the user to enter the date in DD/MM/YYYY, time in 24 hour and the new PSI value
    # Make sure the format is (DD/MM/YYYY hh:mm) refer to the given PSI data excel file
    # Compare the (DD/MM/YYYY hh:mm) in the data frame and get the row information
    # Use index.tolist() method to get the row index value based on the input(date and time)
    # *Use loc[row_index, [direction]] or at[row_index, direction] methods to change the value of the PSI

    # Add your codes....

  elif choice == '5':
    # save excel file pd.to_excel(XXXX_new.xlsx)

    # Add your codes....

  else:
   # use break

   # Add your codes....