# Defines the organic compound identification function
def organic_identification(structuralFormula):

    structuralFormula = structuralFormula.upper()
    compoundName = ""

    # Defines chain prefixes
    chainPrefixArray = [" ", "meth", "eth", "prop", "but", "pent", "hex", "hept", "oct", "non", "dec"]

    # Checks if compound is a hydrocarbon
    hydrocarbon = True
    alkane = True
    hydrocarbonArray = ["C", "H", "2", "3", "(", ")", "4", "5", "6", "7", "8", "9"]
    characterCompositionArray = [0 for i in range(len(hydrocarbonArray))]

    for char in structuralFormula:
        if char not in hydrocarbonArray:
            hydrocarbon = False

        else:
            characterCompositionArray[hydrocarbonArray.index(char)] += 1

            # Checks if compound is an alkane
            if char in hydrocarbonArray[4:]:
                alkane = False


    if alkane:
        compoundName = chainPrefixArray[characterCompositionArray[0]] + "ane"


    return compoundName

print(organic_identification("ch3ch2ch2ch2ch2ch3"))


# MAIN PROGRAM

# from flask import Flask, request
# from markupsafe import escape
#
# app = Flask(__name__)
#
# from flask import render_template
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)