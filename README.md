# speak2write:

This is a special library which is build to convert speech from spoken format to written format.

For example: " I have two dollars" should be conerted to "I have 2$"

The solution of the problem consists of many layers of functions, each doing its own stuff.

## Features Implemented:
- 1-  Preprocessing the input.
      
      Given the input in raw form. This module helps speech data to get into better format for the conversion.
      
- 2-  Text2integer will convert numbers in words format to their respective number format.
      
      Two hundred = 200
      
 - 3-  Currency Converter will convert given currency in text foramt into its currency format.
 
       5 dollars = 5$
       
## Features to be implemented:

- Reading data from any format. Currently we can only give spoken text data in string format.
- We have to take care of text Abbreventions such as 'dunno' should be converted to 'do not know', etc.
- Pauses in speech must be handled.
- fillers in speech must be handled.
- same word occuring more than one time one after the other must be handled.
