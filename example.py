from spoken2writ import currency,text2int,preprocess_text


spoken_text = """ Hey, did you know that - the summer break is coming? Amazing right!! It’s only 5 more days!!"""


# The preprocess_text module will perform various functions like removing whitespaces,decontracting etc.
print(preprocess_text().prepro(spoken_text))
#Output will be: “Hey did you know that the summer break is coming Amazing right Its only 5 more days”

# The text2int module will convert any spoken number into its numerical form.
spoken_text = """seven billion one hundred million thirty one thousand three hundred thirty seven """

print(text2int().text2num(spoken_text))
#Output will be: 7100031337

#The currency modelu will convert currency dollar to its numerical form.
spoken_text = '5'
print(currency().tocurrency(spoken_text))

#Output will be: $5

