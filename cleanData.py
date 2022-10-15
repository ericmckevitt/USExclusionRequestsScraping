def cleanDataByClassName(data, className):
    """Clean data by class name.

    Args:
        data (eTree._Element): The HTML to be parsed.
        className (str): Class name.

    Returns:
        Cleaned data in JSON.
    """
    
    if className == 'portstable':

        output = ""

        children = data.findChildren('tr')
        for i, child in enumerate(children):

            # Get the text of the child
            child_text = child.text
            # Get the td children
            td_child = child.findChildren('td')
            td = td_child[1]
            
            # Get the value of the input
            input = td.findChildren('input')
            value = input[0].get('value')

            # Format the output
            if i < len(children) - 1:
                output += child_text + ": " + value + ", "
            else:
                output += child_text + ": " + value
        return output
