#https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
#This code is taken from above source.
class text2int:

    """Given a number in words format it will convert into number format."""
    """seven billion one hundred million thirty one thousand three hundred thirty seven gets converted to 7100031337"""
      def text2num(textnum, numwords={}):
          if not numwords:
            units = [
              "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
              "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen",
            ]

            tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

            scales = ["hundred", "thousand", "million", "billion", "trillion"]

            numwords["and"] = (1, 0)
            for idx, word in enumerate(units):    numwords[word] = (1, idx)
            for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
            for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

          current = result = 0
          for word in textnum.split():
              if word not in numwords:
                raise Exception("Illegal word: " + word)

              scale, increment = numwords[word]
              current = current * scale + increment
              if scale > 100:
                  result += current
                  current = 0

          return result + current

