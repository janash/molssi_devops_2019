"""
string_util.py
A sample repo for the 2019 MolSSI Software Fellow Bootcamp

Misc. string processing functions
"""

def title_case(sentence):
    """
    Convert a string to title case.

    Title case means that the first character of every word is capitalized and the rest are lowercase.

    Parameters
    ----------
    sentence: string
        String to be converted to title case

    Returns
    -------
    title_case_sentence: string
        String converted to title case

    Examples
    --------
    >>> title_case(ThIS iS a StRing tO be COnverted.)
        'This Is A String To Be Converted.'
    """

    # Check that input is string
    if not isinstance(sentence, str):
        raise TypeError("Input argument must be of type string.")

    # Error if empty string
    if len(sentence) == 0:
        raise ValueError("Cannot apply title function to empty string.")

    # Error if string of whitespaces
    if len(sentence.split()) == 0:
        raise ValueError("Cannot apply title function to string of white spaces.")

    new_fields = []
    fields = sentence.split()
    for i in range(len(fields)):
        new_fields.append(fields[i][0].upper() + fields[i][1:].lower())

    title_case_sentence = ''
    for item in new_fields:
        title_case_sentence += item + ' '

    return title_case_sentence[:-1]
