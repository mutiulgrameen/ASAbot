with open('FinalDFTrain.csv', 'r') as f_in, open('my_file.txt', 'w') as f_out:
    # 2. Read the CSV file and store in variable
    content = f_in.read()
    # 3. Write the content into the TXT file
    f_out.write(content)